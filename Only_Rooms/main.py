from db.user_db import UserInDB
from db.user_db import database_users, generator
from db.rooms_db import RoomsInDB
from db.rooms_db import update_room, get_room, database_rooms
from models.user_models import UserIn, UserOut
from models.rooms_models import RoomIn, RoomOut
from typing import Dict, List
from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.get("/",)
def find_all_rooms():
    return "Bienvenido a OnlyRooms"


@app.get("/rooms/", response_model=Dict[int, RoomsInDB])
async def get_all_rooms():
    return database_rooms


@app.get("/rooms/{id_habitacion}")
async def get_room_id(id_habitacion: int):
    room_in_db = get_room(id_habitacion)
    if room_in_db == None:
        raise HTTPException(status_code=404, detail="La habitación no existe")
    room_out = RoomOut(**room_in_db.dict())
    return room_out


@app.get("/users/", response_model=List[UserInDB], response_model_exclude={"username","password"})
async def get_all_users():
    return database_users


@app.post("/users/", response_model=UserInDB)
async def save_user(user_in_db: UserInDB):
    generator["id_usuario"] = generator["id_usuario"] + 1
    user_in_db.id_usuario = generator["id_usuario"]
    database_users.append(user_in_db)
    return user_in_db


@app.put("/users/{id_usuario}")      
async def update_user(id: int, user_in_db: UserInDB):
    
    try:
        database_users[id] = user_in_db
        return database_users[id]
    
    except:
        raise HTTPException(status_code=404, detail="No existe el usuario")
        
    
    return user_in_db


@app.delete("/users/{id_usuario}")
async def delete_user(id: int):
    
    try:
        obj = database_users[id]
        database_users.pop(id)
        return obj
    
    except:
        raise HTTPException(status_code=404, detail="Usuario no existe")