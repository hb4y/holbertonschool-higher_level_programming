#!/usr/bin/python3
"""
Change the name of a State
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
    state = s.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    s.commit()
    s.close()
