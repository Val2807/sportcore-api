from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from datetime import datetime
from sqlalchemy.orm import declarative_base

from app.db import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)

    team_id = Column(Integer, nullable=False)

    position = Column(String, nullable=True)
    weight = Column(Float, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


# class Player:
#     def __init__(self, first_name, last_name, birth_date, team_id, position=None, weight=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birth_date = birth_date
#         self.position = position
#         self.team_id = team_id
#         self.weight = weight
