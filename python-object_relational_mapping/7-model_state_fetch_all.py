#!/usr/bin/python3
"""
A script that lists all state class objects from the database hbtn_0e_6_usa.
"""


import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    for i in states:
        print(f'{i.id}: {i.name}')

    session.commit()
    session.close()
