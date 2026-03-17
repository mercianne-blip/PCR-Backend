from fastapi import FastAPI
from pydantic import BaseModel
from database import engine, Base, SessionLocal
from models import PCRProtocol

Base.metadata.create_all(bind=engine)

app = FastAPI()


class PCRProtocolCreate(BaseModel):
    denaturation_temp: float
    annealing_temp: float
    denaturation_time: int
    annealing_time: int
    cycles: int


@app.get("/")
def read_root():
    return {"message": "PCR backend connected"}


@app.get("/protocols")
def get_protocols():
    db = SessionLocal()
    try:
        protocols = db.query(PCRProtocol).all()
        return protocols
    finally:
        db.close()


@app.post("/protocols")
def create_protocol(protocol: PCRProtocolCreate):
    db = SessionLocal()
    try:
        new_protocol = PCRProtocol(
            denaturation_temp=protocol.denaturation_temp,
            annealing_temp=protocol.annealing_temp,
            denaturation_time=protocol.denaturation_time,
            annealing_time=protocol.annealing_time,
            cycles=protocol.cycles
        )
        db.add(new_protocol)
        db.commit()
        db.refresh(new_protocol)
        return new_protocol
    finally:
        db.close()