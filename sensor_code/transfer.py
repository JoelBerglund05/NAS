import requests
import sense_hat
from sensor import humidity




data = {
    'humidity' : humidity,
    'location' : 'swe'
}

formResponse = requests.post(
    url = 'http://192.168.0.49:5000/Upload',
    data=data ,
    headers= {
        'Content-Type': 'application/x-www-form-urlencoded'#
    })
