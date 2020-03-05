from flask import Flask, jsonify
from flask_restful import Api
from resources.user import UserResource, UsersResource

from ma import ma
app = Flask(__name__)


app.config.from_pyfile('config.cfg')

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource( UserResource, '/user/<string:name>' )
api.add_resource(UsersResource, '/users')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000)