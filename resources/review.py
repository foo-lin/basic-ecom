from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from models.review import Review
from models.user import User
from schema.review import ReviewSchema
from db import db
from utils.apperror import catchExcption
from utils.customexp import CustomException

review_schema = ReviewSchema()


class ReviewProductResource(Resource):
    
    def get(self, product_id):
        reviews = Review.find_review_by_product(product_id)
        return {
            "reviews": [review_schema.dump(x) for x in reviews]
        }
     
    @jwt_required 
    @catchExcption
    def post(self, product_id):
        user_id = get_jwt_identity()
        user = User.find_by_id(user_id)
        if user:
            data = request.get_json()
            data['user_id'] = user_id
            data['product_id'] = product_id
            
            review = Review.find_review(user_id, product_id)
            if review:
                raise CustomException('User already reviewed this product', 400)
            
            review = review_schema.load(data,session=db.session)
            review.save_to_db()
            return review_schema.dump(review)
        raise CustomException('Please provide a valid user', 400)
    
    def patch(self, product_id):
        pass
            