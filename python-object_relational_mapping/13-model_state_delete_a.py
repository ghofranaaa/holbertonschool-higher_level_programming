#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find and delete all states with a name containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.contains('a')).all()
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
