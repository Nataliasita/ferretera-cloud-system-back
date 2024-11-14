from datetime import datetime

class Inventario:
    def __init__(self, inventario_id: int, producto_id: int, cantidad_disponible: int, fecha_actualizacion: datetime):
        self.inventario_id = inventario_id
        self.producto_id = producto_id
        self.cantidad_disponible = cantidad_disponible
        self.fecha_actualizacion = fecha_actualizacion