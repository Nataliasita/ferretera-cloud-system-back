import httpx
from fastapi import APIRouter, HTTPException
from app.models.inventory import InventarioCreate, TransaccionCreate
from app.services.inventory_service import get_inventarios, create_inventario, get_transacciones_por_inventario, create_transaccion

router = APIRouter()

@router.get("/inventarios/")
async def list_inventarios():
    try:
        return await get_inventarios()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Error al obtener inventarios")

@router.post("/inventarios/")
async def add_inventario(inventario: InventarioCreate):
    try:
        return await create_inventario(inventario.dict())
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Error al crear inventario")

@router.get("/transacciones/{inventario_id}")
async def list_transacciones(inventario_id: int):
    try:
        return await get_transacciones_por_inventario(inventario_id)
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Error al obtener transacciones")

@router.post("/transacciones/")
async def add_transaccion(transaccion: TransaccionCreate):
    try:
        return await create_transaccion(transaccion.dict())
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Error al crear transacción")