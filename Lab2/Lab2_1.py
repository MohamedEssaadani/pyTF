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
from flask import Flask, render_template
from pathlib import Path
from utils.getTodayDate import getTodayDate
import time

# create map object
map = folium.Map(location=[33.5555, -7.7777], zoom_start=2)

# will create a Map.html in directory
map.save("templates/Map.html")

# start a web server using flask
# __name__  = this app
# deploy current app with flask
app = Flask(__name__)


# render map
@app.route("/")
def hello_world():
    return render_template("Map.html")


# call bot
@app.route("/bot")
def covid_bot():
    getState()
    return "<h1> Hello Bot </h1>"


# get covid state from covidmaroc.ma
def getState():
    response = ''
    while response == '':
        try:
            filename = Path("covid_state" + getTodayDate() + ".pdf")
            url = "https://www.covidmaroc.ma/Documents/BULLETIN/" + getTodayDate() + ".COVID-19.pdf"
            print(url)
            response = requests.get(url, verify=False)
            filename.write_bytes(response.content)
            print(response.content)
            break
        except Exception as e:  # work on python 3.x
            print(e)
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue


# start the server
app.run()
