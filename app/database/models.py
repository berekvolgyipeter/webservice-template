from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String, CheckConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class Driver(Base):
    __tablename__ = "drivers"

    name = Column(String, nullable=False, unique=True, primary_key=True)
    team = Column(String, nullable=False)

    created_at: datetime = Column(DateTime, default=datetime.now)
    last_update: datetime = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # Establish a one-to-many relationship with Result
    results = relationship("Result", back_populates="driver")

    __table_args__ = (
        UniqueConstraint('name', 'team', name='unique_name_team'),
    )

    def to_dict(self):
        return {
            "name": self.name,
            "team": self.team
        }


class Result(Base):
    __tablename__ = "results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    grand_prix = Column(String, nullable=False)
    position = Column(Integer, nullable=True)

    driver_name = Column(String, ForeignKey('drivers.name'))
    driver = relationship("Driver", back_populates="results")

    created_at: datetime = Column(DateTime, default=datetime.now)
    last_update: datetime = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        CheckConstraint('position > 0', name='positive_value_check'),
        UniqueConstraint('grand_prix', 'position', name='unique_grand_prix_position'),
        UniqueConstraint('grand_prix', 'driver_name', name='unique_grand_prix_driver_name'),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "grand_prix": self.grand_prix,
            "position": self.position,
            "driver_name": self.driver_name
        }
