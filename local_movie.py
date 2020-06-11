import json

import pymongo
import requests

import config 

client = pymongo.MongoClient(config.MONGO_URL)
db = client.pytest

