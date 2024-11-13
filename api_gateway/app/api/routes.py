from fastapi import APIRouter
from app.api.user_routes import router as user_router

# Crear un enrutador principal para organizar todas las rutas
router = APIRouter()

# Registrar las rutas de usuarios bajo el prefijo "/users"
router.include_router(user_router, prefix="/users")