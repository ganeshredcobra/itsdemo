from itertools import islice
from flask import render_template
from flask import request
from app import app
import requests
 
values =[]
title = "sample app"

@app.route('/')
@app.route('/index')
def index():
  if not values:
     return "Please send data to this application..."
  else:
     display_items = ["Timestamp","Voltage","Current", "Resistance", "Battery", "Vehicle speed","Diagnostic message","Engine speed", "Engine oil","Coolant level"] 
     return render_template("index.html", data=values, display_items = display_items)
  
  

@app.route('/data', methods=['POST'])
def push_data(): 
    print (request.json)
    values.append(request.json)
    return "success.."

@app.route('/data', methods=['GET'])
def fetch_data(): 
    if not values:
       return "Please send data to this application..."
    else:
       display_items = ["Timestamp","Voltage","Current", "Resistance", "Battery", "Vehicle speed","Diagnostic message","Engine speed", "Engine oil","Coolant level"]     
       return render_template("index.html",title=title, data=values, display_items = display_items)


