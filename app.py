import os

import pandas as pd
import numpy as np

import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

# # reflect an existing database into a new model
# Base = automap_base()

# # reflect the tables
# Base.prepare(engine, reflect=True)

# print(str(Base.classes))

# # Save table reference to a variable
# Yelp_info = Base.classes.yelp_info

# # Create the session link   
# session = Session(engine)

#################################################
# Routes
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
   


    # # Create a dictionary from the row data and append to a list of zone_data
   
    #     zone_dict = {}
    #     zone_dict["id"] = field1
    #     zone_dict["Restaurant"] = RestaurantName
    #     zone_dict["Phone"] = PhoneNumber
    #     zone_dict["Address"] = Address
    #     zone_dict["City"] = States
    #     zone_dict["Category"] = Category
    #     restaurant.append(zone_dict)

    return jsonify(restaurant)


if __name__ == "__main__": 
    app.run()
