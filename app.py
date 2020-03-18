from flask import Flask, jsonify
from flask_restful import Api
from resources.address import AddressListResource, AddressIdResource
from resources.user import UserResource,UserListResource 
from resources.category import CategoryIdResource
from resources.category import CategoryListResource
from resources.product import ProductCagegoryResource, ProductListResource
from resources.review import ReviewProductResource
from blueprints.auth import auth_blueprint
from ma import ma
from flask_jwt_extended import JWTManager, get_jwt_claims, jwt_required

app = Flask(__name__)


app.config.from_pyfile('config.cfg')

api = Api(app)

@app.before_first_request
def create_tables():
    print('first request')
    db.create_all()



jwt = JWTManager(app=app)



app.register_blueprint(auth_blueprint, url_prefix="/api/v1")


api.add_resource( UserResource, '/api/v1/user/<string:name>' )
api.add_resource(UserListResource, '/api/v1/user')

api.add_resource(AddressListResource, '/api/v1/address')
api.add_resource(AddressIdResource,'/api/v1/address/<int:_id>' )

api.add_resource(CategoryIdResource, '/api/v1/category/<int:_id>')
api.add_resource(CategoryListResource, '/api/v1/category')

api.add_resource(ProductCagegoryResource, '/api/v1/category/<int:category_id>/product')
api.add_resource(ProductListResource, '/api/v1/product')

api.add_resource(ReviewProductResource, '/api/v1/product/<int:product_id>/review')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000)