# Notes App MVP (Backend)

A simple **single-user Notes API** built as an educational MVP to practice backend development with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, following a **layered architecture**.

The project intentionally keeps scope small and explicit, focusing on clean separation of concerns and correct data flow.

---

## 🎯 Scope

### ✅ What the system does
- Create notes
- List all notes
- Get a single note by ID
- Update a note
- Delete a note

### ❌ Out of scope
- Authentication / authorization
- Multi-user support
- Offline mode
- Native mobile apps
- Database migrations (no Alembic for now)

---

## 🧱 Tech Stack

- **Python** 3.14
- **FastAPI**
- **SQLAlchemy** 2.x
- **PostgreSQL**
- **psycopg** 3 + psycopg-binary
- **python-dotenv**
- **Uvicorn**
- Virtual environment (`venv`)

---

## 🗂️ Project Structure

```text
app/
└── backend/
    ├── api/              # FastAPI routers (HTTP layer)
    ├── core/             # Configuration (env, settings)
    ├── db/               # SQLAlchemy base and session
    ├── models/           # ORM models
    ├── repositories/     # Database access (CRUD)
    ├── schemas/          # Pydantic schemas (DTOs)
    ├── services/         # Business logic (minimal for MVP)
    ├── main.py           # App entrypoint
    ├── .env              # Environment variables (not committed)
    └── requirements.txt

```
## ⚠️ Important

This project does **not** use `app.` as an import prefix.  
All imports are relative to `app/backend`.

**Example:**

```python
from core.config import DATABASE_URL
from db.session import get_db
```

---

## 🗄️ Database

The database is PostgreSQL, created manually (no migrations yet).

**Table:** notes

```sql
CREATE TABLE notes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title VARCHAR(200) NOT NULL,
  content VARCHAR(5000) NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

There are sample notes already inserted for testing.

---

## ⚙️ Configuration

Create a `.env` file inside `app/backend/`:

```env
DATABASE_URL=postgresql+psycopg://postgres:PASSWORD@localhost:5432/postgres
```

If `DATABASE_URL` is missing, the app will **fail fast on startup**.

---

## 🚀 How to Run the Backend

### 1) Activate virtual environment (PowerShell)

```powershell
. .\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies

```powershell
pip install -r requirements.txt
```

### 3) Run the server

```powershell
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## 📚 API Documentation (Swagger)

FastAPI automatically exposes interactive docs.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

You can test the full CRUD:

- GET /notes
- POST /notes
- GET /notes/{note_id}
- PUT /notes/{note_id}
- DELETE /notes/{note_id}

---

## 🩺 Health Checks

### API health

```
GET /health
```

Response:

```json
{ "status": "ok" }
```

### Database health

```
GET /health/db
```

Response:

```json
{ "db": "ok" }
```

---

## 🧠 Architecture Overview

The backend follows a layered architecture:

```
HTTP Request
   ↓
api/ (FastAPI routers)
   ↓
services/ (business orchestration)
   ↓
repositories/ (SQLAlchemy CRUD)
   ↓
PostgreSQL
```

### Design rules

- api/ handles HTTP concerns (status codes, validation errors)
- repositories/ handle database access only
- services/ contain business rules (kept minimal in this MVP)
- main.py only wires the application together
