from pydantic import BaseModel

class RoomIn(BaseModel):
    id_habitacion: int
    
    
class RoomOut(BaseModel):
    id_habitacion: int
    numero: int
    piso: int
    descripcion: str
    caracteristicas: str
    precio_diario: int
    tipo: str