from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID

from models.note import Note
from schemas.note import NoteCreate, NoteUpdate


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
