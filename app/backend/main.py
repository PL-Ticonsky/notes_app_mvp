from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from db.session import get_db

app = FastAPI()


@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"db": "ok"}

@app.get("/health")
def health_api():
    return {"Status":" josue y jd"}