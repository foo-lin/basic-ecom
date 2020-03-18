from flask_restful import Resource
from flask import request
from models.category import Category
from schema.category import CategorySchma
from utils.apperror import catchExcption
from utils.customexp import CustomException


category_schema = CategorySchma()


class CategoryIdResource(Resource):
    
    @catchExcption
    def get(self, _id):
        category = Category.find_by_id(_id)
        if category:
            
            return {'category': category_schema.dump(category)}
        raise CustomException('Category not found', 404)
        
    def delete(self, _id):
        category = Category.find_by_id(_id)
        if category:
            category.delete_from_db()
        return {
            "status":'ok'
        }
    
    def patch(self, _id):
        category = Category.find_by_id(_id)
        for key, value in request.get_json().items():
            setattr(category,key, value)
        category.save_to_db()
        return Category.find_by_id(_id)
        
        
class CategoryListResource(Resource):
    
    def post(self):
        category = category_schema.load(request.get_json())  
        category.save_to_db()
        return category_schema.dump(category)

    def get(self):
        return {
            'categories': [category_schema.dump(x) for x in Category.query.all()]
        }