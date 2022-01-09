from pymongo.encryption import _DATA_KEY_OPTS
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from fastapi.templating import Jinja2Templates
import sqlalchemy
from sqlalchemy import and_
import re
import pandas as pd
import numpy as np

from bson import ObjectId

class Social(BaseModel):
    _id: ObjectId
    #datasource: str
    keywords: str
    content: str

import pandas as pd
import uvicorn

from pymongo import MongoClient



app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main(request: Request):
    social = []
    datas = connection()
    
    #select_data_frame[['keywords','content']]
    return templates.TemplateResponse("main.html", {"request":request,"data":datas})

def connection():
    mgdb_host = 'mongodb.net'
    # mgdb_host = '140.115.53.142'
    mgdb_port = '27017'
    mgdb_username = 'operator'
    #test
    mgdb_password = ''

    mgdb_database = 'ESG'
    mgdb_collection = 'news_content'
    #mgdb_collection = 'test'
    print('mongodb+srv://%s:%s@%s/%s' % (mgdb_username, mgdb_password, mgdb_host, mgdb_database))
    # It has no datas here now, so change to original database first.
    client = MongoClient('mongodb+srv://%s:%s@%s/%s' % (mgdb_username, mgdb_password, mgdb_host, mgdb_database),connect = False)
    #DBconnect = "mongodb+srv://%s:%s@%s/%s' % (mgdb_username, mgdb_password, mgdb_host, mgdb_database)"

    #client = MongoClient(DB_connection)
    #client = MongoClient(DBconnect)
    db = client[mgdb_database]
    collection = db[mgdb_collection]
    key = input("key issue:")

    data = collection.find({"content": re.compile(key)})
    select_data_frame = pd.DataFrame(data)
    return select_data_frame




