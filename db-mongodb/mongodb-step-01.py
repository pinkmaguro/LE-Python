from pymongo import MongoClient
import numpy as np
from datetime import datetime


def step01():
    # 커넥션 생성
    clinet = MongoClient('localhost', 27017)
    # DB 생성
    db = clinet.test
    db.inventory.insert_one(
    {"item": "canvas",
     "qty": 100,
     "tags": ["cotton"],
     "size": {"h": 28, "w": 35.5, "uom": "cm"}})

    cursor = db.inventory.find({"item": "canvas"})
    print(cursor)

if __name__ == '__main__':
    step01()