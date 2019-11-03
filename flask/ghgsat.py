from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Conversion factor between one degree latitude and metres
import math
FACTOR = 1852 * 60

def conversion(latitude, longitude):
    north = latitude + 2500 / FACTOR
    south = latitude - 2500 / FACTOR
    west = longitude - 5000 / (FACTOR * math.cos(math.radians(latitude)))
    east = longitude + 5000 / (FACTOR * math.cos(math.radians(latitude)))

    return (west, south, east, north)

def generate_png_request(west, south, east, north):
    scale = 99220
    addr = 'https://render.openstreetmap.org/cgi-bin/export?bbox={:f},{:f},{:f},{:f}&scale={:d}&format=png'.format(west, south, east, north, scale)
    return addr

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/map')
def map():
    latitude = float(request.args['latitude'])
    longitude = float(request.args['longitude'])
    west, south, east, north = conversion(latitude, longitude)
    addr = generate_png_request(west, south, east, north)
    return redirect(addr)
