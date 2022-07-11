from dateutil import parser

import pymongo
from pymongo import MongoClient

import pandas as pd


# In[2]:


def get_db():
    
    # mongodb atlas url to connect python to mongodb using pymongo
#     CONNECTION_STRING = "mongodb+srv://ada_k:Hjp6GTVnw47jU0qc@kj.mongodb.net/myFirstDatabase"
    CONNECTION_STRING = "mongodb+srv://ada_k:Hjp6GTVnw47jU0qc@kj.r7a6p.mongodb.net/myFirstDatabase"

#     "mongodb+srv://M220-student:M220-password@mflix.thya5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create db for our example
    return client['user_shopping_list']
    
# Get the database
dbname = get_db()

# create collection in python
collection_name = dbname["user_1_items"]

# inserting many docs at once
item_1 = {
"_id" : "U1IT00001",
"item_name" : "Blender",
"max_discount" : "10%",
"batch_number" : "RR450020FRG",
"price" : 340,
"category" : "kitchen appliance"
}

item_2 = {
"_id" : "U1IT00002",
"item_name" : "Egg",
"category" : "food",
"quantity" : 12,
"price" : 36,
"item_description" : "brown country eggs"
}

collection_name.insert_many([item_1,item_2])


# add a datefield
expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
item_3 = {
"item_name" : "Bread",
"quantity" : 2,
"ingredients" : "all-purpose flour",
"expiry_date" : expiry
}
collection_name.insert_one(item_3)

# python querying

# Get db using get_database
dbname = get_db()

# Create a new collection
collection_name = dbname["user_1_items"]

item_details = collection_name.find()
for item in item_details:
    print(item)
#     print(item['item_name'], item['category'])


# handle nans with pandas
# convert the dictionary objects to dataframe
items_df = pd.DataFrame(item_details)

# see the magic
items_df


#indexing in pymongo
item_details = collection_name.find({"category" : "food"})
item_details


category_index = collection_name.create_index("category")
category_index




