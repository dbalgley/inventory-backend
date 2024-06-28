from app.models import db

class Bin(db.Model):
    __tablename__ = 'bin'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
    
    location = db.relationship('Location', back_populates='bins')
    items = db.relationship('Item', back_populates='bin', cascade='all, delete-orphan')