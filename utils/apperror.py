from marshmallow import ValidationError
from functools import wraps
from utils.customexp import CustomException

def catchExcption(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
           return func(*args, **kwargs)
        except  ValidationError as err:
            return err.messages
        except CustomException as err:
            return {'error': err.message}, err.statusCode
        
    return inner