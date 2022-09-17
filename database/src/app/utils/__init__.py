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

