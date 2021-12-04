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
# create map object
map = folium.Map(location=[33.5555, -7.7777], zoom_start=2)

# will create a Map.html in directory
map.save("templates/Map.html")

# start a web server using flask
# __name__  = this app
# deploy current app with flask
app = Flask(__name__)

file_name = "covid16112020 (1).json"

# render
@app.route("/", methods=['GET'])
def hello_world():
    # get countries from json
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


# get covid state from covidmaroc.ma
#def getState():
    #response = ''
    #while response == '':
    #   try:
            # file name to save
    #       filename = Path("covid_state" + getTodayDate() + ".pdf")
            # file source
    #       url = "http://www.covidmaroc.ma/Documents/BULLETIN/" + getTodayDate() + ".COVID-19.pdf"
            # get response
    #       response = requests.get(url, verify=False)
            # write the response content(pdf) to current directory
    #       filename.write_bytes(response.content)
    #       break
    #   except Exception as e:
            # catch error
    #       print(e)
    #       print("Connection refused by the server..")
    #       print("Let me sleep for 5 seconds")
    #       print("ZZzzzz...")
    #       time.sleep(5)
    #       print("Was a nice sleep, now let me continue...")
#       continue


# start the server
app.run()