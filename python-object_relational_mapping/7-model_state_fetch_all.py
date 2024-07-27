#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main(username, password, dbname):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', echo=False)
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    try:
        states = session.query(State).order_by(State.id.asc()).all()
        
        for state in states:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()
