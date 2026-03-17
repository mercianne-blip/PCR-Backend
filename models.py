from sqlalchemy import Column, Integer, Float
from database import Base

class PCRProtocol(Base):
    __tablename__ = "pcr_protocols"

    id = Column(Integer, primary_key=True, index=True)
    denaturation_temp = Column(Float)
    annealing_temp = Column(Float)
    denaturation_time = Column(Integer)
    annealing_time = Column(Integer)
    cycles = Column(Integer)