from flask import request
from flask import Blueprint
from schema.user import UserSchema
from utils.apperror import catchExcption
from utils.customexp import CustomException
from models.user import User
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token

user_schema = UserSchema()
auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route('/login', methods=['POST'])
@catchExcption
def login():
    data = request.get_json() 
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        raise CustomException('Please provide username or password', 401)
    
    user = User.find_by_username(username)
    if user:
        if safe_str_cmp(user.password, password):
            access_token = create_access_token(identity=user.id, fresh=True, expires_delta=False)
            refrest_token = create_refresh_token(user.id)
            return {'access_token':access_token, 'refresh_token': refrest_token } 
        else:
            raise CustomException('Plese provide a valid password', 401)
    else:
        raise CustomException('User does not exist', 401)
    return {34:45}
    
@auth_blueprint.route('/signup')
def register():
    return {45:45}

@auth_blueprint.route('/me')
def get_me():
    return {}