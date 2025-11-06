from flask import Blueprint, jsonify, current_app
from dynaconf import settings


main = Blueprint("main",__name__)


@main.route("/")
def index():

    return jsonify(

        {
            "enviroment": current_app.config["ENV_FOR_DYNACONF"],
            "debug": current_app.config["DEBUG"],
            "database_url": current_app.config["DATABASE_URL"],
            "path_process": current_app.config["PATH_PROCESS"]
        }
    )