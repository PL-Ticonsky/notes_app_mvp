from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


"""
schemas/note.py

Responsabilidad:
- Definir contratos de entrada/salida (Pydantic) para la API.
- Validar tamaños y requerimientos:
  - title: 1..200
  - content: 0..5000
- Separar modelos:
  - NoteCreate: para POST
  - NoteUpdate: para PUT/PATCH (campos opcionales)
  - NoteRead: salida hacia el cliente

Detalles:
- `from_attributes=True` permite convertir desde objetos ORM (`models.Note`)
  hacia `NoteRead` sin mapear manualmente.
"""


class NoteBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(default="", max_length=5000)


class NoteCreate(NoteBase):
    pass


class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    content: str | None = Field(default=None, max_length=5000)


class NoteRead(NoteBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
