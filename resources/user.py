from flask_restful import Resource
from flask import request
from models.user import UserModel
from schema.user import UserSchema
from marshmallow import ValidationError
user_schema = UserSchema()
from db import db

class UserResource(Resource):
    def get(self, name):
        user = UserModel.find_by_username(name)
        
        if user:
            return user_schema.dump(user)
        return {'message': 'user not found'}, 400
    
class UsersResource(Resource):
    def post(self):
        try:
            user = user_schema.load(request.get_json())
            user.save_to_db()
            return {"ok": 23}        
            
        except ValidationError as err:
            return err.messages
        