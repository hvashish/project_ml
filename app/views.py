from flask import *

from app import app
views = Blueprint('views', __name__)
@app.route('/')
@app.route('/index')
def index():
    return '<h1> Hello Mona!, I am going to create a first ML project<h1>'