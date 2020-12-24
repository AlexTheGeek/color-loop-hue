#!/bin/python3
#Alexis Brunet alias AlexTheGeek
####################
## HUE COLOR LOOP ##
####################

import time
import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, request
app = Flask(__name__)

STARTING = '{"on":true,"bri":254,"xy":[0.3523,0.144],"effect":"colorloop"}'
ENDING = '{"effect": "none"}'
OFF = '{"on":false}'

env_path = join(dirname(__file__), 'env')
load_dotenv(env_path)

ip = os.getenv('IP')
api = os.getenv('API')
group = os.getenv('GROUP')

def appel(data, grp):
    headers = {'Content-Type': 'application/json', }
    response = requests.put(
        'http://'+ip+'/api/'+api+'/groups/'+grp+'/action/', headers=headers, data=data)


@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName != 'monstermash':
        if deviceName == 'start':
            appel(STARTING, group)
            return '<h1>Color Loop START</h1>', {'Content-Type': 'text/html'}
        if deviceName == 'stop':
            appel(ENDING, group)
            return '<h1>Color Loop STOP</h1>', {'Content-Type': 'text/html'}
        if deviceName == 'off':
            appel(OFF, group)
            return '<h1>Color Loop TURN OFF</h1>', {'Content-Type': 'text/html'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
