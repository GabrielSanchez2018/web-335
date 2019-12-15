# Author: Richard Krasso
# Edit: Gabriel Sanchez
# Date: 12/15/2019
# Exercise: 9.3

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(

    {"employee_id": "0000015"},

    {

        "$set": {

            "email": "gjsanchez@my365.bellevue.edu"

        }

    }

)

pprint.pprint(db.users.find_one({"employee_id": "0000015"}))