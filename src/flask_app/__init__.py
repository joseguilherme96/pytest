from flask import Flask
from flask_app.routes import main
from dynaconf import  FlaskDynaconf
from pathlib import Path

def create_app():

    app = Flask(__name__)
    settings_path  = Path(__file__).parent / "settings.toml"

    FlaskDynaconf(app,settings_files=[str(settings_path)])
  
    app.register_blueprint(main)  
  
    return app