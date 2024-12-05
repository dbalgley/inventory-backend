from app.models.location import Location
from app.models import db

def get_all_locations():
    return Location.query.all()

def get_location_by_id(location_id):
    return Location.query.get(location_id)

def add_location(data):
    new_location = Bin(
        name=data['name'],
        description=data.get('description')
    )
    db.session.add(new_location)
    db.session.commit()

def update_location(location_id, data):
    location = Location.query.get(location_id)
    if not location:
        return None
    
    location.name = data.get('name', location.name)
    location.description = data.get('description', location.description)
    db.session.commit()

    return location

def delete_location(location_id):
    location = Location.query.get(location_id)
    if not location:
        return None
    db.session.delete(location)
    db.session.commit()

    return location
    
## Relationships

def get_bins_by_location(location_id):
    location = Location.query.get(location_id)
    if location:
        return location.bins
    return None

def get_items_by_location(location_id):
    location = Location.query.get(location_id)
    if location:
        return location.items
    return None