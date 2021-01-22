#importamos clases
from flask import Blueprint
#importamos funciones
from flask import render_template

page = Blueprint('page', __name__,)


@page.route('/')
def index():
    return render_template('index.html')