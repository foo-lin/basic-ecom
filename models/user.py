from db import db

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
        
    @classmethod
    def find_by_username(cls, name):
        return UserModel.query.filter_by(username=name).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        print('sdf')
        
    def __repr__(self):
        return f"User <{self.username}>"