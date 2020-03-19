from ma import ma
from models.order import Orders, Status
from marshmallow_enum import EnumField

class OrderSchema(ma.ModelSchema):
    status = EnumField(Status, by_value=True)
    class Meta:
        model = Orders
        dump_only = ('status','id')
        include_fk = True