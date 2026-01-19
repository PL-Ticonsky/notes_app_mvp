from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID

from models.note import Note
from schemas.note import NoteCreate, NoteUpdate


"""
repositories/note_repository.py

Responsabilidad:
- Capa de acceso a datos (DAL).
- Ejecuta operaciones CRUD contra PostgreSQL usando SQLAlchemy ORM.
- NO maneja HTTP, NO decide códigos de estado, NO lanza HTTPException.
  Solo retorna modelos `Note` (o None) y realiza commits.

Dependencias:
- `db: Session` viene de `Depends(get_db)` en la capa API.
- Usa SQLAlchemy `select` para listados y `db.get()` para búsqueda por PK.

Notas:
- `list_notes` ordena por `updated_at` descendente para mostrar lo más reciente primero.
"""


class NotesRepository:
    def list_notes(self, db: Session) -> list[Note]:
        stmt = select(Note).order_by(Note.updated_at.desc())
        return list(db.scalars(stmt).all())

    def get_note(self, db: Session, note_id: UUID) -> Note | None:
        return db.get(Note, note_id)

    def create_note(self, db: Session, data: NoteCreate) -> Note:
        note = Note(title=data.title, content=data.content)
        db.add(note)
        db.commit()
        db.refresh(note)
        return note

    def update_note(self, db: Session, note: Note, data: NoteUpdate) -> Note:
        if data.title is not None:
            note.title = data.title
        if data.content is not None:
            note.content = data.content

        db.commit()
        db.refresh(note)
        return note

    def delete_note(self, db: Session, note: Note) -> None:
        db.delete(note)
        db.commit()
