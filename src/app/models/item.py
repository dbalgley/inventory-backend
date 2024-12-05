from app.models import db

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    category = db.Column(db.String(120))
    image_url = db.Column(db.String(200))
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
    bin_id = db.Column(db.Integer, db.ForeignKey('bin.id'), nullable=True)

    location = db.relationship('Location', back_populates='items')
    bin = db.relationship('Bin', back_populates='items')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "image_url": self.image_url,
            "description": self.description,
            "created_at": self.created_at
        }
