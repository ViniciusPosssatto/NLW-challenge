from flask import Blueprint


games = Blueprint('games', __name__, url_prefix="/games")


@games.route("/games", methods=['GET'])
def list_all_games():
    return {}, 200
