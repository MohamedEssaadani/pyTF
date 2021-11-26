# COVID-TRACKER BOT
# pip install requests
# pip install BeautifulSoup4
# pip install pandas
# pip install folium
# pip install flask

import requests
from bs4 import BeautifulSoup
import pandas
import folium
from flask import Flask, render_template, request
from pathlib import Path
from utils.getTodayDate import getTodayDate
import time
import json
from flask_pymongo import PyMongo

# create map object
map = folium.Map(location=[33.5555, -7.7777], zoom_start=2)

# will create a Map.html in directory
map.save("templates/Map.html")

# start a web server using flask
# __name__  = this app
# deploy current app with flask
app = Flask(__name__)

# Connect to mongodb
mongodb_client = PyMongo(app, uri="mongodb+srv://essaadani:essaadani@cluster0.4bfd9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db

file_name = "covid16112020 (1).json"

# render
@app.route("/", methods=['GET'])
def hello_world():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def result():
    country1 = request.form["country1"]
    country2 = request.form["country2"]
    country3 = request.form["country3"]
    print('COUNTRIES')
    print(country1, country2, country3)

    casesCountry1 = getCases(country1)
    casesCountry2 = getCases(country2)
    casesCountry3 = getCases(country3)
    print('CASES')
    print(casesCountry1, casesCountry2, casesCountry3)

    deathsCountry1 = getDeaths(country1)
    deathsCountry2 = getDeaths(country2)
    deathsCountry3 = getDeaths(country3)
    print('DEATHS')
    print(deathsCountry1, deathsCountry2, deathsCountry3)

    dateLabels = getDates(country1)
    print('Dates')
    print(dateLabels)
    return render_template("index.html", country1= country1, country2=country2, country3=country3, casesCountry1=casesCountry1, casesCountry2=casesCountry2, casesCountry3=casesCountry3, deathsCountry1= deathsCountry1, deathsCountry2= deathsCountry2, deathsCountry3= deathsCountry3, dateLabels = dateLabels)

def getCases(country):
    with open(file_name) as json_file:
        jsonData = json.load(json_file)
        casesList = []
        for record in jsonData['records']:
            if record['countryterritoryCode']==country:
                casesList.append(int(record['cases']))

    return (list(reversed(casesList)))


def getDeaths(country):
    with open(file_name) as json_file:
        jsonData = json.load(json_file)
        deathsList = []
        for record in jsonData['records']:
            if record['countryterritoryCode']==country:
                deathsList.append(int(record['deaths']))

    return (list(reversed(deathsList)))

def getDates(country):
    with open(file_name) as json_file:
        jsonData = json.load(json_file)
        dateRepList = []
        for record in jsonData['records']:
            if record['countryterritoryCode']==country:
                dateRepList.append(record['dateRep'])

    return (list(reversed(dateRepList)))
# call bot
@app.route("/bot")
def covid_bot():
    # getState()
    return "<h1> Hello Bot </h1>"


# start the server
app.run()