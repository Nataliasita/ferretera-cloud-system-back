import os

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "password"), 
    "database": os.getenv("DB_NAME", "mi_base_de_datos"),
}