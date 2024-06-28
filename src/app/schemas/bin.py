from app.schemas import ma
from app.models.bin import Bin

class BinSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bin
        load_instance = True

    location = ma.Nested('LocationSchema', many=False, only=['id'])
    items = ma.Nested('ItemSchema', many=True, only=['id'])