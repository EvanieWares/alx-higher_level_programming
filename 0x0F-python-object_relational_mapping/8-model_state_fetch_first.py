#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker

if __name__ == '__main__':
    username, password, db_name = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)
    session = scoped_session(
        sessionmaker(
            bind=engine
        )
    )

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(first_state.id, first_state.name, sep=": ")
