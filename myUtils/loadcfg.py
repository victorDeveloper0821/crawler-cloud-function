from dotenv import load_dotenv
from pymongo import MongoClient
import os

# 从 .env 文件加载环境变量
load_dotenv()

def get_config(key):
    """获取指定配置的值"""
    return os.getenv(key)

def getMongoClient():
    """ 取得 MongoDB 設定值 """
    Mongo_Uri = get_config('MONGO_URI')
    try:
        return MongoClient(Mongo_Uri)
    except: 
        raise RuntimeError('Missing MONGO_URI Settings')
