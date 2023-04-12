from flask import Flask, jsonify, request, Blueprint, send_from_directory
from config import Config
from flask_mysqldb import MySQL
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)


from app import routes