from pymongo import MongoClient
import DateUtil
import os

def get_config(key):
    """获取指定配置的值"""
    return os.environ.get(key,'Key Not set')

def getMongoClient():
    """ 取得 MongoDB 設定值 """
    Mongo_Uri = get_config('MONGO_URI')
    try:
        return MongoClient(Mongo_Uri)
    except: 
        raise RuntimeError('Missing MONGO_URI Settings')

def getCollection(prefix, yesterday):
    """ Get MongoDB Collection """
    if prefix is None or type(prefix) is not str:
        prefix = ''
    # get collection name in yesterday or not
    if yesterday:
        return prefix + '_' + DateUtil.getDateWithFormat(DateUtil.yesterday(),"%y%m%d")
    else:
        return prefix + '_' + DateUtil.getDateWithFormat(DateUtil.getNow(),"%y%m%d")

    