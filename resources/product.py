from flask import request
from flask_restful import Resource
from models.product import Product
from models.category import Category
from schema.product import ProductSchema
from utils.apperror import catchExcption
from utils.customexp import CustomException
from utils.apiFeatures import ApiFeature


product_schema = ProductSchema()

class ProductCagegoryResource(Resource):
    
    @catchExcption
    def post(self, category_id):
        load_data = request.get_json()
        product = product_schema.load(load_data)
        product.category_id = category_id
        product.save_to_db()
        return product_schema.dump(product)
    
    @catchExcption
    def get(self, category_id):
        category = Category.find_by_id(category_id)
        query = ApiFeature(category.products, request.args, Product).sort().filter().paginate()
        print(request.args)
        if category:
            return {'products': [product_schema.dump(x) for x in query.query.all()]}
        raise CustomException(f"category with id {category_id} not found", 404)


class ProductListResource(Resource):
    
    def get(self):
        products = [product_schema.dump(x) for x in Product.query.all()]
        return {'products': products}