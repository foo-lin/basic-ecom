from ma import ma
from models.review import Review

class ReviewSchema(ma.ModelSchema):
    class Meta:
        model = Review
        include_fk = True