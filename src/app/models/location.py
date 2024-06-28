from app.models import db

class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    items = db.relationship('Item', back_populates='location', cascade='all, delete-orphan')
    bins = db.relationship('Bin', back_populates='location', cascade='all, delete-orphan')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at
        }