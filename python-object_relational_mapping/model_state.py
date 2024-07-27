#!/usr/bin/python3
"""
This module contains a State class and an instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):
    """
    A state class that links to the MySQL table states.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)
