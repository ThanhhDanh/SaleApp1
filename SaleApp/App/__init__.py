from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy

import SaleApp.App

app = Flask(__name__)

app.secret_key='uhiuyg7yt'

app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/saleapp1?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)





