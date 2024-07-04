# crud.py
from sqlalchemy.orm import Session
from models import Locality, Property
from schemas import PropertyCreate, PropertyUpdate

def create_property(db: Session, property: PropertyCreate):
    db_property = Property(**property.dict())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def get_properties_by_locality(db: Session, locality_id: int):
    return db.query(Property).filter(Property.locality_id == locality_id).all()

def update_property(db: Session, property_id: int, property_update: PropertyUpdate):
    db_property = db.query(Property).filter(Property.id == property_id).first()
    if db_property:
        db_property.name = property_update.name
        db_property.owner_name = property_update.owner_name
        db_property.locality_id = property_update.locality_id
        db.commit()
        db.refresh(db_property)
    return db_property

def delete_property(db: Session, property_id: int):
    db_property = db.query(Property).filter(Property.id == property_id).first()
    if db_property:
        db.delete(db_property)
        db.commit()
    return db_property
