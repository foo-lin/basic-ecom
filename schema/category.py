from ma import ma
from models.category import Category

class CategorySchma(ma.ModelSchema):
    class Meta:
        model = Category
        load_only = ('products',)
        dump_only = ('id','slug')