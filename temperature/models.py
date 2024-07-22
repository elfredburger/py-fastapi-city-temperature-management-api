from sqlalchemy import Column, Integer, String, ForeignKey
from cities.models import City
from sqlalchemy.orm import relationship

from database import Base

class Temperature(Base):
    __tablename__ = "temperatures"
    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Integer)
    city_id = Column(Integer, ForeignKey("cities.id"))
    city = relationship(City)
    date_time = Column(String)

