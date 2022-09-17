from jwt import encode
from flask import current_app

from src.app.models.ad import Ad
from src.app.models.game import Game


def exist_user_discord(discord):
    if Ad.query.filter_by(discord=discord).first():
        return True
    return False


def exist_game(name):
    if Game.query.filter_by(name=name).first():
        return True
    return False


def generate_jwt(payload):
    token = encode(payload, current_app.config['SECRET_KEY'], 'HS256')
    return token
