from ma import ma
from models.category import Category

class CategorySchma(ma.ModelSchema):
    class Meta:
        model = Category
        dump_only = ('id','slug')