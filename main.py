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
try: 
    from pymongo import MongoClient
except: 
    print('error occur program exit ')

def youBikeCrawler():
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    res = requests.get(youbike_url)
    res.raise_for_status()
    print(res.json())

if __name__ == '__main__':
    youBikeCrawler()

