from app.database import utils as db_utils
from app.schemas.drivers import DriversIn
from app.schemas.results import ResultsIn


DRIVERS = [
    {
        "name": "Mika Hakkinen",
        "team": "Mclaren Mercedes"
    },
    {
        "name": "Michael Schumacher",
        "team": "Ferrari"
    },
]

RESULTS = [
    {
        "grand_prix": "1998 Australia",
        "position": 1,
        "driver_name": "Mika Hakkinen"
    },
    {
        "grand_prix": "1998 Australia",
        "position": None,
        "driver_name": "Michael Schumacher"
    },
    {
        "grand_prix": "1998 Brasil",
        "position": 1,
        "driver_name": "Mika Hakkinen"
    },
    {
        "grand_prix": "1998 Brasil",
        "position": 3,
        "driver_name": "Michael Schumacher"
    },
]


if __name__ == "__main__":
    for driver in DRIVERS:
        db_utils.add_driver(DriversIn(**driver))

    for result in RESULTS:
        db_utils.add_result(ResultsIn(**result))
