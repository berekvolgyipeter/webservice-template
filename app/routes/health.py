from flask import Blueprint


api = Blueprint('health', __name__, url_prefix="/")


@api.get("")
def list_drivers() -> tuple[dict, int]:
    return {"status": "OK"}, 200
