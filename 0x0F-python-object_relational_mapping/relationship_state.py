#!/usr/bin/python3
"""
Contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, Relationship
Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = Relationship("City", back_populates="state", passive_deletes=True)
