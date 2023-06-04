from flask import Flask,request
import requests


url = 'http://192.168.0.49:5000/Upload'

data = {
    'humidity' : 22,
    'location' : 'swe'
}

formResponse = requests.post(
    url+'/Upload',
    data=data,
    headers= {
        'Content-Type': 'application/x-www-form-urlencoded'

    })

