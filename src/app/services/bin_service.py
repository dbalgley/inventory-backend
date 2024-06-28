from app.models.bin import Bin
from app.models import db

def get_all_bins():
    return Bin.query.all()

def get_item_by_id(bin_id):
    return Bin.query.get(bin_id)

def add_bin(data):
    new_bin = Bin(
        name=data['name'],
        description=data.get('description')
    )
    db.session.add(new_bin)
    db.session.commit()

    return new_bin

def update_bin(bin_id, data):
    bin = Bin.query.get(bin_id)
    if not bin:
        return None
    
    bin.name = data.get('name', bin.name)
    bin.description = data.get('description', bin.description)
    db.session.commit()

    return bin

def delete_bin(bin_id):
    bin = Bin.query.get(bin_id)
    if not bin:
        return None
    db.session.delete(bin)
    db.session.commit()

    return bin

## Relationships

def get_items_by_bin(bin_id):
    bin = Bin.query.get(bin_id)
    if bin:
        return bin.items
    return None