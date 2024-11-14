from datetime import datetime
from typing import Optional

class Transaccion:
    def __init__(self, transaccion_id: int, inventario_id: int, producto_id: int, tipo_transaccion: str, cantidad: int, fecha_transaccion: datetime, usuario_id: Optional[int]):
        self.transaccion_id = transaccion_id
        self.inventario_id = inventario_id
        self.producto_id = producto_id
        self.tipo_transaccion = tipo_transaccion
        self.cantidad = cantidad
        self.fecha_transaccion = fecha_transaccion
        self.usuario_id = usuario_id