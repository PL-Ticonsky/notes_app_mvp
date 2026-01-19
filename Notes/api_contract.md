# API Contract – Notes MVP

Content-Type: `application/json`  
System type: Single-user  
Authentication: None  

---

## Principal Resource: Note

### Note Attributes (Response)
- `id`: uuid
- `title`: string (max 200 chars)
- `content`: string (max 5000 chars)
- `created_at`: datetime (ISO 8601)
- `updated_at`: datetime (ISO 8601)

Example:
```json
{
  "id": "0f5b8a3b-7f2c-4c41-9a8b-2ad0e3b3f1f0",
  "title": "My note",
  "content": "Some text",
  "created_at": "2026-01-19T12:30:00Z",
  "updated_at": "2026-01-19T12:30:00Z"
}
```

# CreateNoteInput

### Request Body

```json
{
  "title": "My note",
  "content": "Some text"
}
```

---

## Fields Specification

### title
- Required: yes
- Type: string
- Length: 1..200 characters
- Spaces are trimmed before validation

---

### content
- Required: no
- Type: string
- Length: 0..5000 characters
- If not sent, it is saved as an empty string: ""
- null is not allowed
  - If sent as null → validation error

---

## Validation Errors

HTTP 400 – VALIDATION_ERROR is returned if:

- title is missing
- title is empty or contains only spaces
- title has more than 200 characters
- content is null
- content has more than 5000 characters
- title or content are not strings

## Response 

201 - ok papaito 


# UpdateNoteInput

### Request Body

```json
{
  "title": "My note",
}
```

---

## Fields Specification

### title
- Required: yes
- Type: string
- Length: 1..200 characters
- Spaces are trimmed before validation

---

## Validation Errors

HTTP 400 – VALIDATION_ERROR is returned if:

- title is missing
- title is empty or contains only spaces
- title has more than 200 characters
- content is null
- content has more than 5000 characters
- title or content are not strings

## Response 

201 - ok papaito 
```json

{
  "title": "My note",
  "content": "Some text"
}
```
---
# GetNote 

### Request Body

```json
{
    "id":"Note id"
}
```

---

## Fields Specification



---

### id
- Required: id
- Type: uuid
- Length: 0..5000 characters
- If not sent, it sends a 404 error read below
- null is not allowed
  - If sent as null → validation error

---

## Validation Errors

HTTP 400 – VALIDATION_ERROR is returned if:

- id is missing

## Response 

302 - ok papaito 






# GetNotes 


### Request body
None 

### Response

**200 OK** (Note[])
```json
[
  {
    "id": "0f5b8a3b-7f2c-4c41-9a8b-2ad0e3b3f1f0",
    "title": "My note",
    "content": "Some text",
    "created_at": "2026-01-19T12:30:00Z",
    "updated_at": "2026-01-19T12:45:00Z"
  }
]
```
---

## Validation Errors

HTTP 400 – VALIDATION_ERROR is returned if:

- id is missing

## Response 

302 - ok papaito 

# Delete note

### Request Body

```json
{
    "id":"Note id"
}
```

---

## Fields Specification



---

### id
- Required: id
- Type: uuid
- Length: 0..5000 characters
- If not sent, it sends a 404 error read below
- null is not allowed
  - If sent as null → validation error

---

## Validation Errors

HTTP 400 – VALIDATION_ERROR is returned if:

- id is missing

## Response 

200 ok


