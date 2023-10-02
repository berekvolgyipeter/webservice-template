from app.schemas.results import ResultsIn
from app. constants import STATUS_OK
from database import utils as db_utils


def list_results(results_in: ResultsIn):
    results = db_utils.list_results(results_in)
    return {**STATUS_OK, "results": [result.to_dict() for result in results]}


def add_result(results_in: ResultsIn):
    db_utils.add_result(results_in)
    return STATUS_OK
