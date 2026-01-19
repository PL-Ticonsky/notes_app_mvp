from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Text, DateTime, func
import uuid
from db.base import Base


"""
models/note.py

Modelo ORM SQLAlchemy para la tabla `notes`.

Campos:
- id: UUID (PK)
- title: string (max 200)
- content: text
- created_at: timestamp con tz (default now())
- updated_at: timestamp con tz (default now(), cambia en update)

Notas:
- `server_default=func.now()` deja que Postgres ponga el timestamp.
- `onupdate=func.now()` actualiza `updated_at` al hacer UPDATE.
"""


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False, default="")
    created_at: Mapped[object] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[object] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
