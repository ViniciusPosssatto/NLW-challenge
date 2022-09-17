from flask import Flask
from src.app.controllers.games import games
from src.app.controllers.ads import ads


def routes(app: Flask):
    app.register_blueprint(games)
    app.register_blueprint(ads)
