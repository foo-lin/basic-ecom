from db import db
from datetime import datetime

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    zip = db.Column(db.String(10), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Address<f{self.user_id}, {self.id}>"

    @classmethod
    def find_by_id(cls, id):
        return Address.query.filter(Address.id == id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    