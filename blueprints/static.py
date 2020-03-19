from flask import request, Blueprint
from models.category import Category
from models.product import Product
from schema.product import ProductSchema
from schema.category import CategorySchma
from utils.apiFeatures import ApiFeature


static_blueprint = Blueprint('static_blueprint', __name__)

product_schema = ProductSchema()

@static_blueprint.route('/five-products-each')
def get_five_products_each():
    data = dict()
    categories = [ x for x in Category.query.all()]
    for category in categories:
        data[category.name] = [product_schema.dump(y) for y in ApiFeature(category.products, {'limit': 5}, Category).paginate().query.all()]
    return data

