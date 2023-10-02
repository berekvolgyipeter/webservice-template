from flask import Blueprint

from app.constants import DEFAULT_RATE_LIMIT
from app.utils import get_params
from app.global_objects import limiter
from app.schemas import drivers as schema
from app.interactors import drivers as interactor


api = Blueprint('drivers', __name__, url_prefix="/drivers")


@api.get("")
@limiter.limit(DEFAULT_RATE_LIMIT)
@get_params
def list_drivers(params: dict) -> (dict, int):
    drivers_in = schema.validate_optional_drivers_in(params)
    response = interactor.list_drivers(drivers_in)
    return response, 200


@api.post("")
@get_params
def add_driver(params: dict) -> (dict, int):
    drivers_in = schema.validate_all_drivers_in(params)
    response = interactor.add_driver(drivers_in)
    return response, 200
