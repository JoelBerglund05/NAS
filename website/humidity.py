import datetime
from flask import Blueprint, render_template, request
from flask_login import current_user
from . import db
from .models import EnviromentDetails


humidityBp = Blueprint('humidity', __name__)

@humidityBp.route('/Upload', methods = ['POST'])
def UploadData():
    humidity_data = request.form['humidity']
    time = datetime.date.today()
    location = request.form['location']
    data = {
        'data': {
            'humidity':humidity_data,
            'location':location,
            'time':time,
        }
    }
    EnviromentDetails(humidity = data[0], location = data[1], dateTime = data[2])
    return data


@humidityBp.route('/viewdata', methods = ['GET',])
def home():
    return render_template('view_data.html')


#mockhumidity = 42.5
#mockdateTime = datetime.date.today()
#mocklocation = 'trät'
#
#request = EnviromentDetails(humidity = mockhumidity, dateTime = mockdateTime, location = mocklocation)
#db.session.add(request)
#db.session.commit()