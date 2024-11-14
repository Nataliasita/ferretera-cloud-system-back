from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TipoTransaccion(str, Enum):
    entrada = 'entrada'
    salida = 'salida'

class InventarioCreate(BaseModel):
    producto_id: int
    cantidad_disponible: int

class TransaccionCreate(BaseModel):
    inventario_id: int
    producto_id: int
    tipo_transaccion: TipoTransaccion
    cantidad: int
    usuario_id: Optional[int] = None