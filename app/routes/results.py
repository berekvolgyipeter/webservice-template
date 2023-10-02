from flask import Blueprint

from app.constants import DEFAULT_RATE_LIMIT
from app.utils import get_params
from app.global_objects import limiter
from app.schemas import results as schema
from app.interactors import results as interactor


api = Blueprint('results', __name__, url_prefix="/results")


@api.get("")
@limiter.limit(DEFAULT_RATE_LIMIT)
@get_params
def list_results(params: dict) -> (dict, int):
    results_in = schema.validate_optional_results_in(params)
    response = interactor.list_results(results_in)
    return response, 200


@api.post("")
@get_params
def add_result(params: dict) -> (dict, int):
    results_in = schema.validate_all_results_in(params)
    response = interactor.add_result(results_in)
    return response, 200
