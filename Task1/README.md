# Problem Satement

1. CRUD Operations on Sales Dataset
Perform CRUD operations on a sales dataset stored in a CSV file. You can choose any Python library or tool for database operations or perform them directly on the CSV file. Implement the following operations:
Create: Insert new records into the dataset.
Read: Retrieve and display specific records from the dataset.
Update: Modify existing records in the dataset.
Delete: Remove specific records from the dataset.
Provide a Python script demonstrating each CRUD operation with relevant comments and explanations.


# Task 1: CRUD Operations on Sales Dataset
# Description
This task demonstrates CRUD operations (Create, Read, Update, Delete) on a sales dataset using Python and Pandas in a Jupyter Notebook.

# Dataset
File name: sales.csv
Source: Downloaded from Kaggle
Sample Columns: Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales


# Requirements
Install the following dependencies:
pip install pandas

# Files in This Folder
sales_crud.ipynb: Jupyter Notebook with all CRUD operations

sales.csv: Dataset file (ensure it's in the same directory)



# CRUD Operations Performed
 1. Create
Added new records to the dataset using pandas.DataFrame.append().

 2. Read
Displayed the first few records using df.head()
Retrieved specific records based on conditions (e.g., where Rank == 3)

3. Update
Updated values in specific columns using index-based access.

4. Delete
Removed rows based on condition.

# Notes
The original dataset remains unchanged unless explicitly saved using df.to_csv().
All operations are in-memory within the Jupyter Notebook.
