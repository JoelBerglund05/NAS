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
    try:
        sql_data = db.session.execute(db.select(EnviromentDetails)).scalars()
        list = ''
        for data in sql_data:
            list += (data.humidity + '% , ' + data.dateTime + ':')
        return render_template('view_data.html', list=list, user=current_user) 
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
