from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: Optional[str] = None  
    nombre: Optional[str] = None
    email: Optional[str] = None
    celular: Optional[str] = None
    rol: Optional[str] = None
    permisos: Optional[List[str]] = [] 
    fecha_creacion: Optional[str] = None
    estado: Optional[str] = None