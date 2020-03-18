from db import db
from datetime import datetime


class Review(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow())

    
    
    @classmethod
    def find_review(cls, user_id, product_id):
        return cls.query.filter(cls.product_id == product_id).filter(cls.user_id==user_id).first()

    @classmethod
    def find_review_by_product(cls, product_id):
        return cls.query.filter(cls.product_id == product_id)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()