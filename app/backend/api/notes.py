
"""
api/notes.py

Router de FastAPI para el recurso "notes".

Responsabilidad:
- Definir endpoints HTTP (CRUD) para notas.
- Validar entrada/salida mediante schemas (Pydantic).
- Traducir casos de negocio simples a respuestas HTTP:
  - 404 si una nota no existe
  - 422 si el body no cumple el schema (lo maneja FastAPI/Pydantic)

Qué NO hace:
- No ejecuta SQL directamente.
- No contiene lógica de persistencia: delega en NotesRepository.

Dependencias:
- `db: Session` proviene de `Depends(get_db)` y se cierra automáticamente al final del request.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from db.session import get_db
from repositories.notes_repository import NotesRepository
from schemas.note import NoteCreate, NoteUpdate, NoteRead

router = APIRouter(prefix="/notes", tags=["notes"])
repo = NotesRepository()


@router.get("", response_model=list[NoteRead])
def list_notes(db: Session = Depends(get_db)):
    """
    Listar todas las notas.

    - Orden: definido por el repositorio (por ejemplo updated_at desc).
    - Retorna: lista de NoteRead.
    """
    return repo.list_notes(db)


@router.get("/{note_id}", response_model=NoteRead)
def get_note(note_id: UUID, db: Session = Depends(get_db)):
    """
    Obtener una nota por ID (UUID).

    - 404 si no existe.
    - Retorna: NoteRead.
    """
    note = repo.get_note(db, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.post("", response_model=NoteRead, status_code=status.HTTP_201_CREATED)
def create_note(data: NoteCreate, db: Session = Depends(get_db)):
    """
    Crear una nota.

    - Body: NoteCreate (title requerido, content opcional).
    - Retorna: la nota creada (incluye id y timestamps).
    """
    return repo.create_note(db, data)


@router.put("/{note_id}", response_model=NoteRead)
def update_note(note_id: UUID, data: NoteUpdate, db: Session = Depends(get_db)):
    """
    Actualizar una nota existente.

    - Body: NoteUpdate (campos opcionales).
    - 404 si no existe.
    - Retorna: la nota actualizada.
    """
    note = repo.get_note(db, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return repo.update_note(db, note, data)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: UUID, db: Session = Depends(get_db)):
    """
    Eliminar una nota.

    - 404 si no existe.
    - 204 si borra correctamente.
    """
    note = repo.get_note(db, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    repo.delete_note(db, note)
    return None
