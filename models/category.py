from slugify import slugify
from db import db
from datetime import datetime
from models.product import Product


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    slug = db.Column(db.String(40), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow())
    photo = db.Column(db.String(80))
    products = db.relationship(Product, backref='category', lazy='dynamic')
    
    def __init__(self, *args, **kwargs):
        kwargs['slug'] = slugify(kwargs['name']) 
        super().__init__(*args, **kwargs)

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter(cls.id == _id).first()

    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


