from random import randrange
from db import db
from slugify import slugify
from datetime import datetime
from enum import Enum
from models.product import Product

class Status(Enum):
    preDis='preparing for dispatch'
    dispatch='dispatch'
    delivered='delivered'
    canceled='canceled'


class Orders(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    price = db.Column(db.Float, nullable=False )
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.Enum(Status), default=Status.preDis)
    tracking_id = db.Column(db.Integer, default=randrange(10000, 300000))
    product = db.relationship(Product, lazy=True)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter(cls.id == _id).first()

    @classmethod
    def commit_session(cls):
        db.session.commit()
    
    def add_to_session(self):
        db.session.add(self)

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()