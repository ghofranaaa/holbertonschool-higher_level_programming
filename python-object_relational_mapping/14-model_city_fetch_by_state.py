#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa.
"""
from model_state import Base, State
from model_city import City
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

    # Fetch all cities, ordered by id
    cities = session.query(City).order_by(City.id).all()

    # Display cities by their state name and city details
    for city in cities:
        state = session.query(State).get(city.state_id)
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
