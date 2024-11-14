# api_gateway/services/inventory_service.py
import httpx
from app.core.config import INVENT_MS_URL

async def get_inventarios():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{INVENT_MS_URL}/api/inventarios/")
    response.raise_for_status()
    return response.json()

async def create_inventario(inventario_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{INVENT_MS_URL}/api/inventarios/", json=inventario_data)
    response.raise_for_status()
    return response.json()

async def get_transacciones_por_inventario(inventario_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{INVENT_MS_URL}/api/transacciones/{inventario_id}")
    response.raise_for_status()
    return response.json()

async def create_transaccion(transaccion_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{INVENT_MS_URL}/api/transacciones/", json=transaccion_data)
    response.raise_for_status()
    return response.json()