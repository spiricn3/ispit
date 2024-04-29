from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router=APIRouter()

@router.get("/device_type/", response_model=List[schemas.MyDevice])
def read_device(db: Session = Depends(get_db)):
    return db.query(models.Device).all()