# Notes API

Minimal Notes application built with FastAPI and PostgreSQL, following a layered architecture and focusing on clarity, correctness, and reproducibility.

This project was developed as an educational MVP to practice backend architecture, database design, and API development in a real-world setup.

---

## Features

- Create notes
- Update notes
- Delete notes
- List all notes
- Retrieve a single note
- Health checks for API and database

Out of scope:
- Authentication
- Multi-user support
- Offline support
- Native mobile apps

---

## Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy 2.x
- PostgreSQL
- psycopg (v3)
- HTML / CSS / Vanilla JavaScript (minimal frontend)

---

## Project Structure

.
├── app/
│   ├── backend/
│   │   ├── api/              # FastAPI routers
│   │   ├── core/             # Configuration
│   │   ├── db/               # Database session and SQL scripts
│   │   ├── models/           # SQLAlchemy models
│   │   ├── repositories/     # Data access layer
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── main.py           # FastAPI entrypoint
│   │   └── requirements.txt
│   └── frontend/
│       ├── index.html
│       ├── styles.css
│       └── app.js
├── db/
│   ├── schema.sql
│   └── seed.sql
├── .env.example
└── README.md

---

## Architecture Overview

The backend follows a layered architecture:

- API layer: HTTP routing and request/response handling
- Service layer: Business logic (kept minimal for this MVP)
- Repository layer: Database access via SQLAlchemy
- Model layer: ORM models mapped to PostgreSQL tables

main.py only wires dependencies and routers.  
It does not contain business logic or direct database access.

---

## Requirements

- Python 3.12+
- PostgreSQL 16+
- pip / venv

---

## Environment Variables

Create a .env file based on .env.example:

DATABASE_URL=postgresql+psycopg://notes_user:notes_pass@localhost:5432/notes_db

---

## Database Setup

Install PostgreSQL:

sudo apt install postgresql postgresql-contrib  
sudo systemctl enable --now postgresql

Create database and user:

sudo -iu postgres psql << 'SQL'
CREATE USER notes_user WITH PASSWORD 'notes_pass';
CREATE DATABASE notes_db OWNER notes_user;
\c notes_db
CREATE EXTENSION IF NOT EXISTS pgcrypto;
SQL

Create schema and seed data:

sudo -iu postgres psql -d notes_db -f db/schema.sql  
sudo -iu postgres psql -d notes_db -f db/seed.sql

---

## Backend Setup

cd app/backend  
python3 -m venv .venv  
source .venv/bin/activate  
pip install -r requirements.txt  
uvicorn main:app --reload

API will be available at:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

---

## Frontend Setup

The frontend is intentionally minimal.

cd app/frontend  
python3 -m http.server 5173

Open:

http://127.0.0.1:5173

---

## API Endpoints (Summary)

GET /notes  
POST /notes  
GET /notes/{id}  
PUT /notes/{id}  
DELETE /notes/{id}  
GET /health  
GET /health/db

---

## Status

This project represents a completed MVP.  
Further extensions (authentication, migrations, tests, Docker) are intentionally left out of scope.
