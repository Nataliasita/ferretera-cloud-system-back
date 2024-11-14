from fastapi import APIRouter, HTTPException
from app.database import get_db_connection
from app.schemas.inventario import Inventario, InventarioCreate
from typing import List

router = APIRouter()

@router.post("/inventarios/", response_model=Inventario)
def create_inventario(inventario: InventarioCreate):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            query = """
            INSERT INTO inventario (producto_id, cantidad_disponible)
            VALUES (%s, %s)
            """
            cursor.execute(query, (inventario.producto_id, inventario.cantidad_disponible))
            conn.commit()
            inventario_id = cursor.lastrowid
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM inventario WHERE inventario_id = %s", (inventario_id,))
            new_inventario = cursor.fetchone()
    finally:
        conn.close()

    if new_inventario is None:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    
    return new_inventario

# Endpoint para obtener todos los inventarios
@router.get("/inventarios/", response_model=List[Inventario])
def get_inventarios():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM inventario")
            inventarios = cursor.fetchall()
    finally:
        conn.close()

    if not inventarios:
        raise HTTPException(status_code=404, detail="No se encontraron inventarios")

    return inventarios