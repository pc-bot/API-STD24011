from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from datetime import date

app = FastAPI()

class Reservations(BaseModel):
    id : int
    Name : str
    phoneNumber : str
    descriptionRoom : str
    dateReservation : date

all_reservation = List[Reservations] = []

@app.get("/booking")
async def getReservations():
    return JSONResponse(status_code=200,content=all_reservation)

@app.post("/nooking")
async def createReservation(Reservation : List[Reservations]):
    all_reservation.append(Reservation)
    return JSONResponse(content=all_reservation, status_code=201)

