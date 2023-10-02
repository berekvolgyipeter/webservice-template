from database import utils as db_utils
from app.schemas.drivers import DriversIn
from app.schemas.results import ResultsIn
from scripts.initial_data import DRIVERS, RESULTS


if __name__ == "__main__":
    for driver in DRIVERS:
        db_utils.add_driver(DriversIn(**driver))

    for result in RESULTS:
        db_utils.add_result(ResultsIn(**result))
