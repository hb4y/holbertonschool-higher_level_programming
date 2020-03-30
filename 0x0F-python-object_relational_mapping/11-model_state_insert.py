#!/usr/bin/python3
"""
Adds the State object "Louisiana"
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    cs = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                     sys.argv[2], sys.argv[3])
    engine = create_engine(cs, pool_pre_ping=True)
    s = Session(engine)
    new_state = State(name='Louisiana')
    s.add(new_state)
    s.commit()
    state = s.query(State).filter_by(name='Louisiana').first()
    print("{}".format(state.id))
    s.close()
