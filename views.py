from flask import Flask,Blueprint,redirect,render_template,jsonify
from flask_login import login_required

views = Blueprint('views', __name__)

@views.route("/", methods=['GET'])
def home():
    
    return render_template('landing_page.html')

@views.route('/welcome', methods=['GET'])
@login_required
def welcome():
    
    return render_template('home.html')