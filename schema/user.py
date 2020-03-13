from ma import ma
from models.user import UserModel
class UserSchema(ma.ModelSchema):
    class Meta:
        model  = UserModel
        load_only =('password', 'role')
        dump_only = ('id',)