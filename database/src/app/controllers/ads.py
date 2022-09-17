from flask import Blueprint


ads = Blueprint('ad', __name__, url_prefix="/ads")


@ads.route("/ads", methods=['GET'])
def list_all_ads():
    return {}, 200
