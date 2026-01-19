from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


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
