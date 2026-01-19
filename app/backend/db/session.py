from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from sqlalchemy.orm import Session
from core.config import DATABASE_URL
"""
db/session.py

Responsabilidad:
- Crear el `engine` SQLAlchemy usando `DATABASE_URL`.
- Configurar `SessionLocal` (sessionmaker).
- Exponer `get_db()` como dependencia de FastAPI:
  entrega una sesión por request y garantiza `db.close()` al final.

Detalles:
- `pool_pre_ping=True` ayuda a detectar conexiones muertas y reestablecer.
"""

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
