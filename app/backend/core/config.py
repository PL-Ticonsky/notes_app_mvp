import os
from dotenv import load_dotenv
"""
core/config.py

Responsabilidad:
- Cargar variables de entorno desde `.env` (python-dotenv).
- Exponer `DATABASE_URL` para la conexión a la base de datos.

Decisión:
- Fallar temprano si falta DATABASE_URL (raise RuntimeError).
  Así no arrancamos el servidor “a medias” y evitamos errores confusos más tarde.

Uso:
- Importar directamente:
  `from core.config import DATABASE_URL`
"""

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Add it to your .env file.")
