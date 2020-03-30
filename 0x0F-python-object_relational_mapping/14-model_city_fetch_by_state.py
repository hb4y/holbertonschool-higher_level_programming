#!/usr/bin/python3
"""
Prints all City objects from the database
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base
from model_state import State
from model_city import City


if __name__ == "__main__":
    cs = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                     sys.argv[2], sys.argv[3])
    engine = create_engine(cs, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    s = Session(engine)
    rs = s.query(City, State).filter(City.state_id == State.id) \
                                   .order_by(City.id).all()
    for city, state in rs:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    s.close()
