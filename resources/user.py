from flask_restful import Resource
from flask import request
from models.user import User
from schema.user import UserSchema
from db import db
from utils.apperror import catchExcption
from utils.customexp import CustomException
from flask_jwt_extended import jwt_required, get_jwt_claims, jwt_optional, get_jwt_identity

user_schema = UserSchema()

class UserResource(Resource):

    @jwt_required
    @catchExcption
    def get(self, name):
        user_id = get_jwt_identity()
        user = User.find_by_username(name)
        if user:
            return user_schema.dump(user)
        raise CustomException(f"user with name {name} does not exits", 404) 

    def delete(self, name):
        user = User.find_by_username(name)
        if user:
            user.delete_from_db()
        return {'status': 'ok'}, 204
    
    @catchExcption
    def patch(self, name):
        user = User.find_by_username(name)
        print(name)
        if user:
            for key, value in request.get_json().items():
                if key not in ['id']:
                    setattr(user, key, value)
            user.save_to_db()
            return {"user": user_schema.dump(user)}
        else:
            raise CustomException(f"user with name {name} does not found", 404)   

class UserListResource(Resource):
    
    def get(self):
        print(self)
        users = User.query.all()
        users_json = [user_schema.dump(x) for x in users]
        return {'users': users_json}
        
    
    @catchExcption
    def post(self):
        user = user_schema.load(request.get_json())
        user.save_to_db()
        return user_schema.dump(user)        
            
        