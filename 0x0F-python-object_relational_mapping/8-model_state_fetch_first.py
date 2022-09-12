#!/usr/bin/python3
"""
list the first State object from a database
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    first_state = session.query(State.id, State.name).first()
    if (first_state is None):
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
