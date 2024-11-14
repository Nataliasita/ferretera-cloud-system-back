from fastapi import APIRouter, HTTPException
from app.database import get_db_connection
from app.schemas.transaccion import Transaccion, TransaccionCreate
from typing import List

router = APIRouter()

@router.post("/transacciones/", response_model=Transaccion)
def create_transaccion(transaccion: TransaccionCreate):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            query = """
            INSERT INTO transaccioninventario (inventario_id, producto_id, tipo_transaccion, cantidad, usuario_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                transaccion.inventario_id,
                transaccion.producto_id,
                transaccion.tipo_transaccion,
                transaccion.cantidad,
                transaccion.usuario_id
            ))
            conn.commit()
            transaccion_id = cursor.lastrowid
            cursor.execute("SELECT * FROM transaccioninventario WHERE transaccion_id = %s", (transaccion_id,))
            new_transaccion = cursor.fetchone()
    finally:
        conn.close()

    if new_transaccion is None:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    
    return new_transaccion

# Endpoint para obtener transacciones de un inventario específico
@router.get("/transacciones/{inventario_id}", response_model=List[Transaccion])
def get_transacciones_por_inventario(inventario_id: int):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM transaccioninventario WHERE inventario_id = %s"
            cursor.execute(query, (inventario_id,))
            transacciones = cursor.fetchall()
    finally:
        conn.close()

    if not transacciones:
        raise HTTPException(status_code=404, detail="No se encontraron transacciones para el inventario especificado")

    return transacciones
