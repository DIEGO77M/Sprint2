from typing import Dict
from pydantic import BaseModel

class RoomsInDB(BaseModel):
    id_habitacion: int
    numero: int
    piso: int
    descripcion: str
    caracteristicas: str
    precio_diario: int
    tipo: str

database_rooms = Dict[int, RoomsInDB]

database_rooms ={
        1: RoomsInDB(**{"id_habitacion":1,
                            "numero": 101,
                            "piso": 1,
                            "descripcion": "Comodo y reconfortante",
                            "caracteristicas": "2 camas, 1 baño",
                            "precio_diario": 50000,
                            "tipo": "Sencilla"}),
    
        2: RoomsInDB(**{"id_habitacion":2,
                            "numero": 102,
                            "piso": 1,
                            "descripcion": "Comodo y reconfortante",
                            "caracteristicas": "2 camas, 1 baño",
                            "precio_diario": 50000,
                            "tipo": "Sencilla"}),
}

def get_room(id_habitacion: int):
    if id_habitacion in database_rooms.keys():
        return database_rooms[id_habitacion]
    else:
        return None
    
def update_room(room_in_db: RoomsInDB):
    database_rooms[room_in_db.id_habitacion] = room_in_db
    return room_in_db