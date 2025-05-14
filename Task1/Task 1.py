#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pandas library 
import pandas as pd


# In[7]:


df = pd.read_csv('C:\\Users\\hp\\Downloads\\archive (8)\\sales.csv')


# In[8]:


#info of dataset
df.info()


# In[9]:


#Top data from dataset
df.head()


# In[10]:


#CRUD Operations 
# Function to Create a new record
def create_record(new_record):
    global df
    new_df = pd.DataFrame([new_record], columns=df.columns)
    df = pd.concat([df, new_df], ignore_index=True)
    print("✅ Record created:")
    print(df.tail(1))  # Print the last inserted row

# Example record to add
new_record = [6, "GTA 6 NEW GAME", "PC", 2025, "Action", "New Publisher", 10.0, 5.0, 1.0, 0.5, 16.5]
create_record(new_record)


# In[22]:


#Read Operation
# Function to read and display the row where Rank is 3
def read_specific_record():
    # Filter the row where Rank is 3
    specific_row = df[df['Rank'] == 3]
    
    # Display the row
    print(specific_row)

# Call the function to display the record with Rank 3
read_specific_record()


# In[19]:


# Function to update a record by Rank value
def update_record(rank_value, updated_record):
    global df
    df.loc[df['Rank'] == rank_value, ['Name', 'Platform', 'Year', 'Genre', 'Publisher', 
                                      'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']] = updated_record
    print(" Record updated:")
    print(df[df['Rank'] == rank_value])  # Display the updated row

# Example update
updated_record = ["Wii Sports", "Wii", 2006, "Sports", "Nintendo", 45.0, 30.0, 4.0, 9.0, 88.0]
update_record(1, updated_record)  # Update record with Rank 1


# In[20]:


df.head()


# In[21]:


# Function to delete a record by Rank value
def delete_record(rank_value):
    global df
    df = df[df['Rank'] != rank_value]  # Remove the row where Rank matches
    print("🗑️ Record deleted:")
    print(df)  # Display the updated DataFrame

# Example delete
delete_record(2)  # Delete record with Rank 2


# In[ ]:




