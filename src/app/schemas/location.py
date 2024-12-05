from app.schemas import ma
from app.models.location import Location

class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location
        load_instance = True

    bins = ma.Nested('BinSchema', many=True, only=['id'])
    items = ma.Nested('ItemSchema', many=True, only=['id'])