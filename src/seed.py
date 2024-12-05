import os
from flask import Flask
from app import create_app
from app.models import db
from app.models.item import Item
from app.models.location import Location
from app.models.bin import Bin

app = create_app()

with app.app_context():
    # Drop all tables and recreate them (optional, only if you want to reset the database)
    db.drop_all()
    db.create_all()

    # Create sample locations
    location1 = Location(name="Warehouse A", description="Main warehouse")
    location2 = Location(name="Warehouse B", description="Secondary warehouse")

    # Add sample locations to the session
    db.session.add(location1)
    db.session.add(location2)

    # Commit to save locations
    db.session.commit()

    # Create sample bins
    bin1 = Bin(name="Bin 1", description="First bin in Warehouse A", location_id=location1.id)
    bin2 = Bin(name="Bin 2", description="Second bin in Warehouse A", location_id=location1.id)
    bin3 = Bin(name="Bin 3", description="First bin in Warehouse B", location_id=location2.id)

    # Add sample bins to the session
    db.session.add(bin1)
    db.session.add(bin2)
    db.session.add(bin3)

    # Commit to save bins
    db.session.commit()

    # Create sample items
    item1 = Item(name="Item 1", description="First item", price=10.0, location_id=location1.id, bin_id=bin1.id)
    item2 = Item(name="Item 2", description="Second item", price=20.0, location_id=location1.id, bin_id=bin2.id)
    item3 = Item(name="Item 3", description="Third item", price=30.0, location_id=location2.id, bin_id=bin3.id)

    # Add sample items to the session
    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)

    # Commit to save items
    db.session.commit()