from api.notes import router as notes_router
from db.session import get_db
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

"""
main.py

Punto de entrada del backend FastAPI.

Responsabilidad:
- Crear la instancia `FastAPI()`
- Montar routers (API)
- Exponer endpoints de salud:
  - /health: confirma que la API responde
  - /health/db: confirma conectividad con PostgreSQL

Nota:
- La lógica de notas vive en `api/`, `services/`, `repositories/`.
  main.py no debe contener lógica de negocio ni SQLAlchemy CRUD.
"""

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5173",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes_router)


@app.get("/health")
def health_api():
    return {"status": "ok"}


@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"db": "ok"}
