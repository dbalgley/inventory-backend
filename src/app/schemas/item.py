from app.schemas import ma
from app.models.item import Item

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instance = True

    location = ma.Nested('LocationSchema', many=False, only=['id'])
    bin = ma.Nested('BinSchema', many=False, only=['id'])