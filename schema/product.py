from ma import ma
from models.product import Product

class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
        dump_only = ('id', 'slug' )