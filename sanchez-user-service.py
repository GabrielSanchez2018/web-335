# Author: Richard Krasso
# Edit: Gabriel Sanchez
# Date: 12/15/2019
# Exercise: 9.2

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {

    "first_name": "Ana",

    "last_name": "Flores",

    "email": "analaura@me.com",

    "employee_id": "0000015",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000015"}))