from ma import ma
from models.address import Address

class AddressSchema(ma.ModelSchema):
    class Meta:
        model = Address
        dump_only = ('id',)