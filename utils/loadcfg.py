from dotenv import load_dotenv
import os

# 从 .env 文件加载环境变量
load_dotenv()

def get_config(key):
    """获取指定配置的值"""
    return os.getenv(key)
