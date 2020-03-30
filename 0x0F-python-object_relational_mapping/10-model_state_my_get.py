#!/usr/bin/python3
"""
prints the State object with the name passed
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
    state = s.query(State).filter_by(name=sys.argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
    s.close()
