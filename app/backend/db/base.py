"""
db/base.py

Define la clase Base para modelos ORM (SQLAlchemy 2.x).
Todos los modelos (ej. Note) heredan de Base para usar el estilo declarativo.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
