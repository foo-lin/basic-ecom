from db import db
from datetime import datetime
from slugify import slugify

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    slug = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, default=0)
    createAt = db.Column(db.DateTime, default=datetime.utcnow() )
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, *args, **kwargs):
        kwargs['slug'] = slugify(kwargs['name'])
        super().__init__(*args, **kwargs)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter(cls.id == _id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter(cls.name == name).first()
    
    def __repr__(self):
        return f"Product<{self.name}>"
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    