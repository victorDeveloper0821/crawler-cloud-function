"""
Helper for youbike loading data from url 

Step1: Initialize connection to MongoDB (Verify connections)
Step2: Ensure that youbike API works fine and fetch data conditionally
Step3: rename and clean data from API
Step4: Insert data to MongoDB (Stored in collection by date)
"""
from datetime import datetime, timedelta
import json 
import requests
from myUtils.loadcfg import getMongoClient

def youBikeCrawler():
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    collName='youbike_'+datetime.now().strftime("%y%m%d")
    res = requests.get(youbike_url)
    res.raise_for_status()
    data = res.json()
    print(data)
    client = getMongoClient()
    
    db = client['youbike']
    collection = db[collName]
    insertMany = collection.insert_many(documents=data)
    if len(insertMany) == len(data):
        return 'Successful'
    else: 
        return 'Error'

if __name__ == '__main__':
    youBikeCrawler()

