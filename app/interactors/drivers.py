from app.schemas.drivers import DriversIn
from app.constants import STATUS_OK
from database import utils as db_utils


def list_drivers(drivers_in: DriversIn):
    drivers = db_utils.list_drivers(drivers_in)
    return {**STATUS_OK, "drivers": [driver.to_dict() for driver in drivers]}


def add_driver(drivers_in: DriversIn):
    db_utils.add_driver(drivers_in)
    return STATUS_OK
