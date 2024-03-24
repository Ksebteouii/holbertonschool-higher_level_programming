#!/usr/bin/python3
"""
Script that prints the State object with the name passed
as an argument from the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(username, password, db_name, state_name):
    """
    Connects to the database and retrieves the State object
    with the specified name.
    """
    # Create the database connection string
    connection_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    # Create the SQLAlchemy engine
    engine = create_engine(connection_str)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the State object with the given name
    state = session.query(State).filter_by(name=state_name).first()

    # Print the State id if found, or "Not found" otherwise
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    # Call the main function
    main(username, password, db_name, state_name)
