from flask import Flask, jsonify
from flask_restful import Api
from resources.user import UserResource,UserListResource 

from ma import ma
app = Flask(__name__)


app.config.from_pyfile('config.cfg')

api = Api(app)

@app.before_first_request
def create_tables():
    print('first request')
    db.create_all()

api.add_resource( UserResource, '/api/v1/user/<string:name>' )
api.add_resource(UserListResource, '/api/v1/user')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000)