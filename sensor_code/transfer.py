import requests
from sense_hat import SenseHat
from sensor import value

while value:
    return humidity



data = {
    'humidity' : value(),
    'location' : 'swe'
}

formResponse = requests.post(
    url = 'http://192.168.0.49:5000/Upload',
    data=data ,
    headers= {
        'Content-Type': 'application/x-www-form-urlencoded'#
    })
