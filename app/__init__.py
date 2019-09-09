from flask import Flask
from flask_bootstrap import Bootstrap
from config import configurations

bootstrap = Bootstrap()

def new_app(config_name):

  app = Flask(__name__)
  app.config.from_object(configurations[config_name])
  bootstrap.init_app(app)

  

  from .main import main as first_blueprint
  app.register_blueprint(first_blueprint)


  return app