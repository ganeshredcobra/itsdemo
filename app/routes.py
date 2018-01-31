from itertools import islice
from flask import render_template
from flask import jsonify
from flask import request
from app import app
import requests

tasks = [
    {
        'id': 1,
        'title': u'Route',
        'From': u'Trivandrum',
		'Dest': u'Kovalam',
		'Via': u'Statue',
		'noStops':7,
     	'done': u'False'
    },
    {
        'id': 2,
        'title': u'Ad',
        'description': u'Smoking is Injurious', 
        'done': u'False'
    },
	{
		'id': 3,
		'stops' : [
		{u'No':0,u'Lat':10,u'Long':15,u'stop':u'tvm'},
		{u'No':1,u'Lat':20,u'Long':25,u'stop':u'statue'},
		{u'No':2,u'Lat':30,u'Long':35,u'stop':u'university'},
		{u'No':3,u'Lat':40,u'Long':45,u'stop':u'pettah'},
		{u'No':4,u'Lat':50,u'Long':55,u'stop':u'airport'},
		{u'No':5,u'Lat':60,u'Long':65,u'stop':u'bypass'},
		{u'No':6,u'Lat':60,u'Long':65,u'stop':u'kovalam'}		
		]
	}
]
 
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
    #return "success.."
    return jsonify(tasks), 201

@app.route('/data', methods=['GET'])
def fetch_data(): 
    if not values:
       return "Please send data to this application..."
    else:
       display_items = ["Timestamp","Voltage","Current", "Resistance", "Battery", "Vehicle speed","Diagnostic message","Engine speed", "Engine oil","Coolant level"]     
       return render_template("index.html",title=title, data=values, display_items = display_items)


