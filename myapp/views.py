#importamos clases
from flask import Blueprint
#importamos funciones
from flask import render_template

page = Blueprint('page', __name__,)

#decorador para ejecutar la funcion, con el codigo 404
@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html', title='bogota')