
# Amazon Product Scraper (Python)
This Python-based scraper allows users to search for a product on Amazon India and extract detailed product information like name, price, and rating for up to 50 items. The results are saved into a clean and structured Excel (.xlsx) file, making it useful for product research, price comparisons, or market analysis.

# Features
✅ Dynamic product search via user input

✅ Scrapes multiple pages to retrieve up to 50 product records

✅ Extracts product names, prices, and ratings

✅ Automatically saves data to a formatted Excel file

✅ Handles missing or unavailable fields gracefully

✅ Implements polite crawling practices (randomized delays)

# Prerequisites
Before running the script, ensure the following are installed:

pip install requests beautifulsoup4 pandas openpyxl
These libraries are used for:

requests: Sending HTTP requests to Amazon's website

BeautifulSoup4: Parsing and extracting data from HTML



# How to Run


Open a terminal or command prompt and navigate to the project directory.

Run the script using:
python product_scraper.py
Enter the product name you want to search (e.g., Laptop, Headphones, Smartphone).

The scraper will:
Fetch product data from Amazon India
Collect up to 50 product listings

Export the results to an Excel file named like amazon_products_Laptop.xlsx



# How It Works (Under the Hood)
The user inputs a product name (e.g., iPhone).

A formatted Amazon search URL is created using the query.

The script loops through search result pages (&page=1, &page=2, etc.).

For each product card (div[data-component-type="s-search-result"]):

Product name is extracted from the title span

Price is gathered from multiple price span classes

Rating is captured from the star icon text

Scraped data is collected in a list of dictionaries and written into an Excel file using pandas.

# Challenges

The challenges faced while developing this scrapper is the Amazon and Flipkart website does not supporting because of security. Somehow Managed to avoid it but it is not permanent solution.
