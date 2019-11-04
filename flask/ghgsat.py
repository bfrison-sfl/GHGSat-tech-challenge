from flask import Flask, app, redirect, render_template, request
from PIL import Image
import requests

app = Flask(__name__)

# Conversion factor between one degree latitude and metres
import math
FACTOR = 1852 * 60

def conversion(latitude, longitude):
    north = latitude + 2500 / FACTOR
    south = latitude - 2500 / FACTOR
    cos_lat = math.cos(math.radians(latitude))
    west = longitude - 5000 / (FACTOR * cos_lat)
    east = longitude + 5000 / (FACTOR * cos_lat)
    # The line below ensures the size of the map in pixel is independent of the
    # latitude
    scale = int(69500 / cos_lat)

    return (west, south, east, north, scale)

def generate_png_request(west, south, east, north, scale):
    addr = 'https://render.openstreetmap.org/cgi-bin/export' + \
        '?bbox={:f},{:f},{:f},{:f}&scale={:d}&format=png'.format(
                west, south, east, north, scale)
    return addr

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    s = requests.Session()
    # To obtain a token;
    s.get('https://www.openstreetmap.org')
    latitude = float(request.args['latitude'])
    longitude = float(request.args['longitude'])
    west, south, east, north, scale = conversion(latitude, longitude)
    addr = generate_png_request(west, south, east, north, scale)
    response = s.get(addr)
    with open('static/images/map.png', 'wb') as m:
        m.write(response.content)
    return render_template('map.html')

@app.route('/plume', methods=['POST'])
def plume():
   plume_file = request.files['plume_file']
   img = Image.open(plume_file)
   bg = Image.open('static/images/map.png')
   bg.paste(img, (0, 0), img)
   bg.save('static/images/plume.png')
   return render_template('plume.html')

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response
