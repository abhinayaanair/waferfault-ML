from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://algorythm:jLnqLVWfxfZPQxQA@cluster0.3seb2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="algorythm"
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\Users\abhin\Desktop\PROJECT\SensorProject\notebooks\wafer_fault.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)