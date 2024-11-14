from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransaccionCreate(BaseModel):
    inventario_id: int
    producto_id: int
    tipo_transaccion: str  # 'entrada' o 'salida'
    cantidad: int
    usuario_id: Optional[int]

class Transaccion(BaseModel):
    transaccion_id: int
    inventario_id: int
    producto_id: int
    tipo_transaccion: str
    cantidad: int
    fecha_transaccion: datetime
    usuario_id: Optional[int]