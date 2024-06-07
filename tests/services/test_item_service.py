from src.app.services.item_service import get_all_items, get_item_by_id, add_item, update_item, delete_item
from src.app.models.item import Item
from src.app.models import db
import pytest

# FILEPATH: /home/dbalgley/Projects/inventory-backend/tests/inventory_backend/app/services/test_item_service.py


# Test get_all_items function
def test_get_all_items():
    # Create some test items
    item1 = Item(name="Item 1", price=10)
    item2 = Item(name="Item 2", price=20)
    item3 = Item(name="Item 3", price=30)
    
    # Add the items to the database
    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.commit()
    
    # Call the get_all_items function
    items = get_all_items()
    
    # Assert that the returned items match the expected items
    assert len(items) == 3
    assert item1 in items
    assert item2 in items
    assert item3 in items

# Test get_item_by_id function
def test_get_item_by_id():
    # Create a test item
    item = Item(name="Test Item", price=50)
    
    # Add the item to the database
    db.session.add(item)
    db.session.commit()
    
    # Call the get_item_by_id function
    retrieved_item = get_item_by_id(item.id)
    
    # Assert that the retrieved item matches the expected item
    assert retrieved_item == item

# Test add_item function
def test_add_item():
    # Create a test item
    item_data = {
        "name": "New Item",
        "price": 100
    }
    
    # Call the add_item function
    added_item = add_item(item_data)
    
    # Assert that the added item exists in the database
    assert Item.query.get(added_item.id) == added_item

# Test update_item function
def test_update_item():
    # Create a test item
    item = Item(name="Old Item", price=200)
    
    # Add the item to the database
    db.session.add(item)
    db.session.commit()
    
    # Update the item's name and price
    updated_data = {
        "name": "Updated Item",
        "price": 300
    }
    update_item(item.id, updated_data)
    
    # Retrieve the updated item from the database
    updated_item = Item.query.get(item.id)
    
    # Assert that the item's name and price have been updated
    assert updated_item.name == updated_data["name"]
    assert updated_item.price == updated_data["price"]

# Test delete_item function
def test_delete_item():
    # Create a test item
    item = Item(name="Item to Delete", price=400)
    
    # Add the item to the database
    db.session.add(item)
    db.session.commit()
    
    # Call the delete_item function
    deleted_item = delete_item(item.id)
    
    # Assert that the deleted item no longer exists in the database
    assert Item.query.get(item.id) is None
    assert deleted_item == item
