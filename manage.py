from myapp import create_app

#permite levantar el servidor apartir de una instancia
from flask_script import Manager

from config import config


config_class = config['development']

myapp = create_app(config_class)

if __name__ == '__main__':
    manager = Manager(myapp)
    manager.run()