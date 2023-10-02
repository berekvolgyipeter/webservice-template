from flask import Blueprint


api = Blueprint('health', __name__, url_prefix="/")


@api.get("")
def list_drivers() -> (dict, int):
    return {"status": "OK"}, 200
