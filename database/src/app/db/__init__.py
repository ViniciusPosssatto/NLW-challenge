import random
import datetime
import requests
from src.app.models.ad import Ad
from src.app.models.game import Game


def populate_db():
    jogos = [
        {"title": "World of warcraft", "url": "https://static-cdn.jtvnw.net/ttv-boxart/18122-144x192.jpg"},
        {"title": "PUBG", "url": "https://static-cdn.jtvnw.net/ttv-boxart/516575-144x192.jpg"},
        {"title": "Valorant", "url": "https://static-cdn.jtvnw.net/ttv-boxart/493057-144x192.jpg"},
        {"title": "CS:GO", "url": "https://static-cdn.jtvnw.net/ttv-boxart/32399_IGDB-144x192.jpg"},
        {"title": "Mir4", "url": "https://static-cdn.jtvnw.net/ttv-boxart/966704637_IGDB-144x192.jpg"},
        {"title": "LoL", "url": "https://static-cdn.jtvnw.net/ttv-boxart/21779-144x192.jpg"},
        {"title": "FIFA22", "url": "https://static-cdn.jtvnw.net/ttv-boxart/1869092879_IGDB-144x192.jpg"},
    ]

    for game in jogos:
        Game.seed(
            title=game["title"],
            banner_url=game["url"]
        )

    users = requests.get('https://randomuser.me/api?nat=br&results=100')

    for user in users.json()['results']:
        Ad.seed(
            name=user['name']['first'] + ' ' + user['name']['last'], 
            hours_playing=random.randint(1,10000), 
            discord=user['email'],
            password="users['login']['salt']",
            week_days=str(random.randint(0,8)), 
            hour_start=random.randint(0,24), 
            hour_end=random.randint(0,24),
            create_at=datetime.date.today(), 
            playing=True, 
            game_id=random.randint(1,7)
        )
