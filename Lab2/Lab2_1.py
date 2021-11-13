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
def hello_bot():
    return "<h1> Hello Bot </h1>"

# start the server
app.run()
