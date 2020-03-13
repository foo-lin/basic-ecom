from db import db
import datetime
from enum import Enum


class UserRole(Enum):
    user='user'
    admin='admin'

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    joined = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    role = db.Column(db.Enum(UserRole), nullable=False)
    photo = db.Column(db.String(80), default="user.jpg")
        
    @classmethod
    def find_by_username(cls, name):
        return UserModel.query.filter(cls.username==name).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    def __repr__(self):
        return f"User <{self.username}>"