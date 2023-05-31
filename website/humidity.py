import datetime
from flask import Blueprint, request
from sense_hat import SenseHat
from . import db
from .models import EnviromentDetails

sense = SenseHat()
sense.clear()

humidityBp = Blueprint('humidity', __name__)
humidity = sense.get_humidity()
print(humidity)

@humidityBp.route('/Upload', methods = ['GET', 'POST'])
def UploadData():
    data = request.json

    mockhumidity = 42.5
    mockdateTime = datetime.date.today()
    mocklocation = 'trät'
    
    request = EnviromentDetails(humidity = mockhumidity, dateTime = mockdateTime, location = mocklocation)
    db.session.add(request)
    db.session.commit()