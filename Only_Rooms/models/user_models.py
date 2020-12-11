from pydantic import BaseModel


class UserIn(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: str
    num_documento: int
    direccion: str
    telefono: int
    email: str
    password: str
    username: str
    
class UserOut(BaseModel):
    id_usuario: int
    nombres: str
    apellidos: str