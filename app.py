import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///whitney.sqlite.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save table reference to a variable
api_data = Base.classes.api

# Create the session link
session = Session(engine)



#################################################
# Routes
#################################################

# API Route
@app.route("/api")
def zones():
    
    # Query the API table
    results = session.query(yelp_info.field1, yelp_info.RestaurantName, yelp_info.PhoneNumber, yelp_info.Address, yelp_info.States, yelp_info.Category).all()

    # Create a dictionary from the row data and append to a list of zone_data
    restaurant = []
    for field1, RestaurantName, PhoneNumber, Address, States, Category in results:
        zone_dict = {}
        zone_dict["id"] = field1
        zone_dict["Restaurant"] = RestaurantName
        zone_dict["Phone"] = PhoneNumber
        zone_dict["Address"] = Address
        zone_dict["City"] = States
        zone_dict["Category"] = Category
        restaurant.append(zone_dict)

    return jsonify(restaurant)
    print


if __name__ == "__main__": 
    app.run()