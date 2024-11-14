from fastapi import FastAPI
from app.routers import inventario, transaccion

app = FastAPI()

app.include_router(inventario.router, prefix="/api")
app.include_router(transaccion.router, prefix="/api")