#!/usr/bin/python3
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = 'cities'
    name = Column(String(128),
                  nullable=False)
    state_id = Column(String(60),
                      ForeignKey('states.id'),
                      nullable=False)
    """
    def __init__(self, *args, **kwargs):
       initializes city
      super().__init__(*args, **kwargs)
    """