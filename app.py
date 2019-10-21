import os

import pandas as pd
import numpy as np

import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#################################################
engine = db.create_engine("sqlite:///whitney.sqlite")
connection=engine.connect()
metadata=db.MetaData()
Yelp_info=db.Table('yelpinfo', metadata, autoload=True, autoload_with=engine)
print(Yelp_info.columns.keys())
        
    # Query the API table
query = db.select([Yelp_info])
ResultProxy=connection.execute(query)
ResultSet=ResultProxy.fetchall()
print(ResultSet[:1])

restaurant = []

for row in ResultSet:
    (field1, RestaurantName, PhoneNumber, Address, States, Category) = row

    zone_dict = {}
    zone_dict["id"] = field1
    zone_dict["Restaurant"] = RestaurantName
    zone_dict["Phone"] = PhoneNumber
    zone_dict["Address"] = Address
    zone_dict["City"] = States
    zone_dict["Category"] = Category
    restaurant.append(zone_dict)

print(restaurant)
# API Route
@app.route("/")
def zones():
   
    return jsonify(restaurant)


if __name__ == "__main__": 
    app.run()
