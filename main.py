# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import Locality, Property
from schemas import PropertyCreate, PropertyUpdate, Property
import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/add_new_property", response_model=Property)
def add_new_property(property: PropertyCreate, db: Session = Depends(get_db)):
    return crud.create_property(db=db, property=property)

@app.get("/fetch_all_properties")
def fetch_all_properties(locality_id: int, db: Session = Depends(get_db)):
    properties = crud.get_properties_by_locality(db=db, locality_id=locality_id)
    if not properties:
        raise HTTPException(status_code=404, detail="Locality not found")
    return properties

@app.put("/update_property_details/{property_id}", response_model=Property)
def update_property_details(property_id: int, property: PropertyUpdate, db: Session = Depends(get_db)):
    db_property = crud.update_property(db=db, property_id=property_id, property_update=property)
    if not db_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property

@app.delete("/delete_property_record/{property_id}")
def delete_property_record(property_id: int, db: Session = Depends(get_db)):
    db_property = crud.delete_property(db=db, property_id=property_id)
    if not db_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return {"message": "Property deleted successfully"}
