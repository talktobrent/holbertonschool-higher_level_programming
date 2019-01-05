#!/usr/bin/python3
""" deletes all State objects with 'a' in their name """


if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = session = Session(engine)

    session.query(State).filter(State.name.like("%a%")).delete(
                                                synchronize_session='fetch')
    session.commit()
    session.close()
