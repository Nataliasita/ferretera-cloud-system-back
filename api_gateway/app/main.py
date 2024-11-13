from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

# Registrar el enrutador principal
app.include_router(router)
