#!/usr/bin/python3
"""
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(username, password, db_name, state_name):
    connection_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(connection_str)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=state_name).first()

    if state is not None:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    main(username, password, db_name, state_name)
