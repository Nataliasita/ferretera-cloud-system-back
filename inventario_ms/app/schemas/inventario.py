from pydantic import BaseModel
from datetime import datetime

class InventarioCreate(BaseModel):
    producto_id: int
    cantidad_disponible: int

class Inventario(BaseModel):
    inventario_id: int
    producto_id: int
    cantidad_disponible: int
    fecha_actualizacion: datetime