#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

from sys import argv

if __name__ == "__main__" and len(argv) == 5:

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.orm.exc import NoResultFound

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)

    try:
        state = session.query(State).filter(State.name == argv[4]).one()
        print(state.id)
    except NoResultFound:
        print("Not found")
    session.close()
