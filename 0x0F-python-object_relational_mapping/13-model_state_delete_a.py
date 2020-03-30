#!/usr/bin/python3
"""
deletes all State objects with a letter
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    cs = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                     sys.argv[2], sys.argv[3])
    engine = create_engine(cs, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    s = Session(engine)
    for state in s.query(State).filter(State.name.contains('a')).all():
        s.delete(state)
    s.commit()
    s.close()
