#!/usr/bin/python3
"""
A script that lists all state class objects from the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, passwd, database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    try:
        states = session.query(State).order_by(State.id.asc()).all()
        
        for state in states:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()
