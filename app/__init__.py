from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

from app.Controllers import Controller
