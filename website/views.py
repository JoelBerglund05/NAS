from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/chatbot')
@login_required
def chatbot():
    return render_template('chatbot.html', user=current_user)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)