-- db/seed.sql
-- Inserts initial notes for local testing.

BEGIN;

INSERT INTO notes (title, content)
VALUES
  ('Welcome', 'This is your first note.'),
  ('Ideas', 'Write ideas here. Keep it simple.'),
  ('Todo', '- Finish README\n- Verify CRUD in Swagger\n- Polish repo structure'),
  ('FastAPI', 'FastAPI provides automatic OpenAPI docs at /docs.'),
  ('PostgreSQL', 'Remember: permissions matter. Your app user must have table privileges.'),
  ('Architecture', 'API -> Service (optional) -> Repository -> DB'),
  ('Testing', 'Manual testing via Swagger is enough for this MVP.'),
  ('Notes', 'Short notes are easier to scan.'),
  ('Seed Data', 'This data is for development only.'),
  ('Done', 'MVP complete.');

COMMIT;
