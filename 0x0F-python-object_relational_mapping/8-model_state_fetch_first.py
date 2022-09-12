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
    Session = sessionmaker(bind=eng)
    session = Session()

    res = session.query(State.id, State.name).first()
    if (res is None):
        print("Nothing")
    else:
        print("{:d}: {}".format(res[0], res[1]))
