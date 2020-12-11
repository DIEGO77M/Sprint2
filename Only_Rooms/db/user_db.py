from typing import List
from pydantic import BaseModel

class UserInDB(BaseModel):
    id_usuario: int = 0
    nombres: str
    apellidos: str
    tipo_documento: str
    num_documento: int
    direccion: str
    telefono: int
    email: str
    password: str
    username: str
    
database_users = {}
generator = {"id_usuario":0}

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.id_habitacion] = user_in_db
    return user_in_db