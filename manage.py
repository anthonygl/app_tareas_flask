from myapp import create_app

#permite levantar el servidor apartir de una instancia
from flask_script import Manager

myapp = create_app()

if __name__ == '__main__':
    manager = Manager(myapp)
    manager.run()