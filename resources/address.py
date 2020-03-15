from flask import request
from flask_restful import Resource
from models.address import Address
from models.user import User
from schema.address import AddressSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.apperror import catchExcption
from utils.customexp import CustomException
from utils.apperror import catchExcption
from utils.customexp import CustomException

address_schema = AddressSchema()


class AddressIdResource(Resource):
    
    @jwt_required
    @catchExcption
    def get(self, _id):
        address = Address.find_by_id(_id)
        if address:
            return address_schema.dump(address)
        raise CustomException('Address not found', 404)
    
    @jwt_required
    @catchExcption
    def patch(self, _id):
        user_id = get_jwt_identity()
        user = User.find_by_id(user_id)
        address = Address.find_by_id(_id)
        user_address = user.addresses.all()
        if address in user_address:
            for key, value in request.get_json().items():
                setattr(address, key, value)
            address.save_to_db()
            return {address: address_schema.dump(address)}
        raise CustomException(f"User cannot update only one's own address", 400)
        
    @jwt_required
    @catchExcption
    def delete(self, _id):
        user_id = get_jwt_identity()
        user = User.find_by_id(user_id)
        address = Address.find_by_id(_id)
        user_address = user.addresses.all()
        if address in user_address:
            address.delete_from_db()
            return {'status': 'ok'}, 204 
        raise CustomException(f"User cannot delete only one's own address", 400)
        

class AddressListResource(Resource):
    
    @jwt_required
    @catchExcption
    def post(self):
        address = address_schema.load(request.get_json())
        user_id = get_jwt_identity()
        address.user_id = user_id
        address.save_to_db()
        return  address_schema.dump(data)
    
    @jwt_required
    def get(self):
       user_id = get_jwt_identity()
       user = User.find_by_id(user_id)
       if user:
           addresses = [address_schema.dump(x) for x in  user.addresses.all()]
           return {'addresses': addresses}