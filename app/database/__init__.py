from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.constants import POSTGRES_URL


Base = declarative_base()
__engine = create_engine(POSTGRES_URL)
__Session = sessionmaker(bind=__engine)


def create_tables():
    # Create the tables based on your model definitions
    # (create tables for all models that are associated with the Base using inheritance)
    Base.metadata.create_all(__engine)


def get_session():
    return __Session()
