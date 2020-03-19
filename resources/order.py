from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from models.order import Orders
from models.user import User
from schema.product import ProductSchema
from schema.order import OrderSchema
from utils.apiFeatures import ApiFeature
from utils.apperror import catchExcption
from utils.customexp import CustomException

order_schema = OrderSchema()
product_schema = ProductSchema()

class OrderResource(Resource):
    
    @jwt_required
    @catchExcption
    def get(self):
        user_id = get_jwt_identity()
        user =  User.find_by_id(user_id)
        if user:
            orders = ApiFeature(user.orders, request.args, Orders).sort().filter().paginate()
            orders_to_return = []
            for order in orders.query.all():
                temp = order_schema.dump(order)
                temp['product'] = product_schema.dump(order.product)
                orders_to_return.append(temp)
            return {"orders": orders_to_return}
        raise  CustomException('Please log in to view order', 400)
    
    @jwt_required
    def post(self):
            user_id = get_jwt_identity()
            orders = request.get_json()['orders']
            for order in orders:
                data = order.copy()
                data['user_id'] = user_id
                data['total'] = data['quantity'] * data['price']
                o = order_schema.load(data)
                o.add_to_session()
            Orders.commit_session()
            return {'status': "success"}

        