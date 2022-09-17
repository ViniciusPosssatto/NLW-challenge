from flask import Blueprint, jsonify, request

from src.app.models.game import Game, games_share_schema
from src.app.utils import exist_game
from src.app.services.game_service import create_game


games = Blueprint('games', __name__, url_prefix="/games")


@games.route("/", methods=['GET'])
def list_all_games():

    query_db_all_games = Game.query.all()
    dict_db_all_games = games_share_schema.dump(query_db_all_games)

    return (dict_db_all_games), 200


@games.route("/create", methods=['POST'])
def create_games():

    body = request.get_json()

    if exist_game(body["discord"]):
        return jsonify({"error": "Esse usuário já existe."}), 400

    response = create_game(**body)

    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 201