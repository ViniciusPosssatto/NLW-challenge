from flask import Blueprint, jsonify, request

from src.app.models.ad import Ad, ads_share_schema
from src.app.utils import exist_user_discord
from src.app.services.ad_service import create_ad


ads = Blueprint('ads', __name__, url_prefix="/ads")


@ads.route("/", methods=['GET'])
def list_all_ads():

    query_db_all_ads = Ad.query.all()
    dict_db_all_ads = ads_share_schema.dump(query_db_all_ads)

    return (dict_db_all_ads), 200

@ads.route("/create", methods=['POST'])
def create_ads():
    
    body = request.get_json()

    if exist_user_discord(body["discord"]):
        return jsonify({"error": "Esse usuário já existe."}), 400

    response = create_ad(**body)

    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 201