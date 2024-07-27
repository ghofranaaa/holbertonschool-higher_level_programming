#!/usr/bin/python3
"""
A script that updates the name of a state object in the database hbtn_0e_6_usa.
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

    # Find the state with id = 2 and update its name
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("Nothing found")

    session.close()
