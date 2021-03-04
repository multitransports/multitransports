from flask import render_template, jsonify

from back.requestsapi import *
import sqlite3

def entry_point():
    return render_template('./app.html')

def hello_world():
    return 'Hello Boug'

def nexttram(station, ville):
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    c.row_factory = sqlite3.Row
    res = requestnexttram(c, station, ville)
    return jsonify(res)

def citystations(ville):
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    c.row_factory = sqlite3.Row
    res = request_city_station(c, ville)
    return jsonify(res)

def line_station(ville, ligne):
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    c.row_factory = sqlite3.Row
    res = request_line_station(c, ville, ligne)
    return jsonify(res)

def next_to_direction(ville, station, ligne, direction):
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    c.row_factory = sqlite3.Row
<<<<<<< HEAD
    res = request_next_to_direction( c, ville, station, ligne, direction)
=======
    res = request_next_to_direction(c, ville, station, ligne, direction)
>>>>>>> 57aa82bd183e61b4156de29818b3e55fa694edd7
    return jsonify(res)