#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """


if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)

    new = State(name="Lousiana")
    session.add(new)
    session.commit()
    print(new.id)

    session.close()
