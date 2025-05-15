import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def get_amazon_products(query, max_products=50):
    """
    Scrapes Amazon search results for the given query and returns up to max_products.
    Handles pagination to collect products from multiple pages.
    """
    headers = {
        # User-Agent to mimic a real browser request
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")
    }
    products = []  # List to store scraped product info
    page = 1       # Start from first search results page

    # Loop through pages until we collect desired number of products
    while len(products) < max_products:
        # Construct URL for the current search results page
        search_url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}&page={page}"
        print(f"Scraping page {page}...")

        try:
            response = requests.get(search_url, headers=headers)

            # Check if Amazon captcha page appeared (blocked)
            if "captcha" in response.text.lower():
                print("Amazon captcha detected - request blocked.")
                break

            # Parse page HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Find all product containers on the page
            results = soup.find_all("div", {"data-component-type": "s-search-result"})

            if not results:
                print("No more search results found.")
                break

            # Loop over each product and extract details
            for product in results:
                # Stop if we reached max_products
                if len(products) >= max_products:
                    break

                # Extract product name/title
                name_tag = product.find("span", class_="a-size-medium a-color-base a-text-normal")
                if not name_tag:
                    h2_tag = product.find("h2")
                    name_tag = h2_tag.find("span") if h2_tag else None
                name = name_tag.text.strip() if name_tag else "N/A"

                # Extract price (whole and fractional parts)
                price_whole = product.find("span", class_="a-price-whole")
                price_fraction = product.find("span", class_="a-price-fraction")

                # Combine whole and fractional price parts if both exist
                if price_whole and price_fraction:
                    price = price_whole.text.strip() + price_fraction.text.strip()
                elif price_whole:
                    price = price_whole.text.strip()
                else:
                    # Sometimes price is in a different span
                    price_span = product.find("span", class_="a-offscreen")
                    price = price_span.text.strip() if price_span else "N/A"

                # Extract product rating if available
                rating_tag = product.find("span", {"class": "a-icon-alt"})
                rating = rating_tag.text.split()[0] if rating_tag else "N/A"

                # Append the product info to the list
                products.append({
                    "Product Name": name,
                    "Price (INR)": price,
                    "Rating": rating
                })

            # Move to next page
            page += 1

            # Polite delay between requests to avoid blocking
            time.sleep(random.uniform(1, 2))

        except Exception as e:
            print(f"Error scraping Amazon on page {page}: {e}")
            break

    return products


def main():
    # Take product query input from user
    query = input("Enter the product to search for: ").strip()
    if not query:
        print("Empty query. Exiting.")
        return

    print(f"Scraping Amazon for '{query}'")

    # Call scraper function to get product data
    products = get_amazon_products(query, max_products=50)

    if not products:
        print("No products found!")
        return

    # Convert list of dicts into a pandas DataFrame
    df = pd.DataFrame(products)

    # Create filename for Excel output
    filename = f"amazon_products_{query.replace(' ', '_')}.xlsx"

    try:
        # Save data to Excel file without index column
        df.to_excel(filename, index=False)
        print(f"Scraped {len(products)} products and saved to '{filename}'.")
    except PermissionError:
        # Handle file write permission errors gracefully
        print(f"Permission denied when saving file '{filename}'. Please close it if it's open and try again.")


if __name__ == "__main__":
    main()
