# ERD – Notes MVP

Este documento define el **modelo de datos** para el MVP de notas y sus reglas en PostgreSQL.
El sistema es **single-user** (no hay tabla de usuarios).

---

## Entities

### 1) notes

A note is the main resource in the system.

#### Attributes

- `id` (PK): UUID
- `title`: VARCHAR(200) NOT NULL
- `content`: VARCHAR(5000) NOT NULL DEFAULT ''
- `created_at`: TIMESTAMPTZ NOT NULL DEFAULT now()
- `updated_at`: TIMESTAMPTZ NOT NULL DEFAULT now()

---

## Entity-Relationship Diagram (Text)

```text
+-------------------------------+
|            notes              |
+-------------------------------+
| id (PK, uuid)                 |
| title (varchar(200), not null)|
| content (varchar(5000), not null, default '') |
| created_at (timestamptz, not null) |
| updated_at (timestamptz, not null) |
+-------------------------------+
