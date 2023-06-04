import datetime
from flask import Blueprint, render_template, request
from flask_login import current_user
from . import db
from .models import EnviromentDetails


humidityBp = Blueprint('humidity', __name__)

@humidityBp.route('/Upload', methods = ['POST', 'GET'])
def UploadData():
    humidity_data = request.form['humidity']
    time_data = datetime.date.today()
    location_data = request.form['location']
    EnviromentDetails(humidity = humidity_data, location = location_data, dateTime = time_data)
    return render_template('upload.html')

@humidityBp.route('/viewdata', methods = ['GET'])
def VeiwData():
    return render_template('view_data.html')


#mockhumidity = 42.5
#mockdateTime = datetime.date.today()
#mocklocation = 'trät'
#
#request = EnviromentDetails(humidity = mockhumidity, dateTime = mockdateTime, location = mocklocation)
#db.session.add(request)
#db.session.commit()