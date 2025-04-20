from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from databases.database import get_db

from Schemas.medicine import MedicineCreate, MedicineUpdate,MedicineOut
from Views.medicine import (
    fetch_medicine_by_id,
    fetch_medicine_by_name,
    fetch_all_medicines,
    create_new_medicine,
    update_existing_medicine,
    delete_medicine_by_id,
)

router = APIRouter()

@router.get("/", response_model=list[MedicineOut])
def get_all_medicines(db: Session = Depends(get_db)):
    return fetch_all_medicines(db)