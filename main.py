#!/bin/python3

import json
import turtle
import urllib.request
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('Amount of people in space:', result['number'])

people = result['people']

for p in people:
  print(p['name'], 'in', p['craft'])
  
  
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude', lat)
print('Longitude', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

# Leeds
lat = 53.800
lon = -1.543

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

time.sleep(10)
