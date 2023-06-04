from curses import flash
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
    data = EnviromentDetails(humidity = humidity_data, location = location_data, dateTime = time_data)
    db.session.add(data)
    db.session.commit()
    return render_template('upload.html', user=current_user)

@humidityBp.route('/viewdata', methods = ['GET'])
def VeiwData():
    return render_template('view_data.html', user=current_user)
