from app.models.item import Item
from app.models import db

def get_all_items():
    return Item.query.all()

def get_item_by_id(item_id):
    return Item.query.get(item_id)

def add_item(data):
    new_item = Item(
        name=data['name'],
        category=data.get('category'),
        image_url=data.get('image_url'),
        description=data.get('description')
    )
    db.session.add(new_item)
    db.session.commit()

    return new_item

def update_item(item_id, data):
    item = Item.query.get(item_id)
    if not item:
        return None
    
    item.name = data.get('name', item.name)
    item.category = data.get('category', item.category)
    item.image_url = data.get('image_url', item.image_url)
    item.description = data.get('description', item.description)
    db.session.commit()
    
    return item

def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return None
    db.session.delete(item)
    db.session.commit()
    
    return item