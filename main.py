"""
Helper for youbike loading data from url 

Step1: Initialize connection to MongoDB (Verify connections)
Step2: Ensure that youbike API works fine and fetch data conditionally
Step3: rename and clean data from API
Step4: Insert data to MongoDB (Stored in collection by date)
"""
from datetime import datetime, timedelta
import json 
import urllib.request
from myUtils.loadcfg import getMongoClient

def youBikeCrawler(request):
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    collName='youbike_'+datetime.now().strftime("%y%m%d")
    with urllib.request.urlopen(youbike_url) as response:
    # 检查响应码是否为 HTTP 200 (OK)
        if response.getcode() == 200:
            # 读取响应体并解码为 UTF-8 字符串
            response_body = response.read().decode('utf-8')
            # 解析 JSON 数据
            data = json.loads(response_body)
        else:
            # 如果响应码不是 200，抛出异常
            raise Exception(f"HTTP Error: {response.getcode()} for {youbike_url}")

    client = getMongoClient()
    
    db = client['youbike']
    collection = db[collName]
    insertMany = collection.insert_many(documents=data)
    if len(insertMany.inserted_ids) == len(data):
        return 'Successful'
    else: 
        return 'Error'

if __name__ == '__main__':
    youBikeCrawler()

