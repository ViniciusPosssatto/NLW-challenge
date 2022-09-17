from src.app.models.ad import Ad
from src.app.models.game import Game


def exist_user_discord(body):
    if Ad.query.filter_by(discord=body).first():
        return True
    return False