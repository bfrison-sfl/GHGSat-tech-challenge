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
