from fastapi import FastAPI
from app.routers import inventario, transaccion
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes. Cambiar a dominios específicos en producción.
    allow_credentials=True,  # Permitir envío de cookies o headers como Authorization
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)


app.include_router(inventario.router, prefix="/api")
app.include_router(transaccion.router, prefix="/api")