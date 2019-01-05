#!/usr/bin/python3
""" changes name of instance with id: 2 to 'New Mexico'  """

from sys import argv

if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.orm.exc import NoResultFound

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)

    try:
        state = session.query(State).filter(State.id == 2).one()
        state.name = "New Mexico"
        session.commit()
    except NoResultFound:
        print("Not found")
    session.close()
