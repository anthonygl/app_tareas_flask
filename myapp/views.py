#importamos clases
from flask import Blueprint
#importamos funciones
from flask import render_template

# a que se importa para poder pindar los atributos de form en el html, para lograr esto 
# se envia la instancia de la clase loginform al template
# en el archivo views se importa login form
from .forms import LoginForm

page = Blueprint('page', __name__,)

#decorador para ejecutar la funcion, con el codigo 404
@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html', title='bogota')


@page.route('/login')
def login():
    # Nueva instancia, para enviar como parametro al template, 
    # ya que template pueda usarlo para pintar los atributos
    form = LoginForm()
    return render_template('auth/login.html', form=form)

