from typing import List, Union, Type
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.models import Base, Driver, Result
from app.constants import POSTGRES_URL
from app.exceptions import DriverNotFound
from app.schemas.drivers import DriversIn
from app.schemas.results import ResultsIn


# Create a SQLAlchemy engine
__engine = create_engine(POSTGRES_URL)

# Create a session to interact with the database
__Session = sessionmaker(bind=__engine)
__session = __Session()


def create_tables():
    # Create the tables based on your model definitions
    # (create tables for all models that are associated with the Base using inheritance)
    Base.metadata.create_all(__engine)


def get_session():
    return __session


def get_driver(name: str) -> Union[Driver, None]:
    session = get_session()
    return session.query(Driver).filter_by(name=name).first()


def list_drivers(drivers_in: DriversIn) -> List[Type[Driver]]:
    session = get_session()
    query = session.query(Driver)
    for key, value in vars(drivers_in).items():
        if value:
            query = query.filter_by(**{key: value})

    return query.all()


def list_results(results_in: ResultsIn) -> List[Type[Result]]:
    session = get_session()
    query = session.query(Result)
    for key, value in vars(results_in).items():
        if value:
            query = query.filter_by(**{key: value})

    return query.all()


def add_driver(drivers_in: DriversIn):
    session = get_session()
    session.add(Driver(**vars(drivers_in)))
    session.commit()


def add_result(results_in: ResultsIn):
    session = get_session()
    driver = get_driver(results_in.driver_name)
    if not driver:
        raise DriverNotFound(results_in.driver_name)
    session.add(Result(**vars(results_in)))
    session.commit()
