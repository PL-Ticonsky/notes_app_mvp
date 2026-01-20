-- db/schema.sql
-- Creates the database schema for the Notes MVP.
-- Assumes you already created the database and enabled pgcrypto.

BEGIN;

-- Required for gen_random_uuid()
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS notes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title VARCHAR(200) NOT NULL,
  content VARCHAR(5000) NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Helpful index for sorting by updated_at
CREATE INDEX IF NOT EXISTS idx_notes_updated_at ON notes (updated_at DESC);

COMMIT;
