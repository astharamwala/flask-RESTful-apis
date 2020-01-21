import os

import logging
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from security import authentication, identify
from resources.item import Item, ItemList
from resources.user import UserRegister, User
from resources.store import Store, StoreList

logger = logging.getLogger("ENV OF LOGGER")

logger.debug("Flask app starts now")
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///myDatabase.db')
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.before_first_request
def create_table():
    db.create_all()


api = Api(app)
app.secret_key = "SomeSecretKey"

jwt = JWT(app, authentication, identify)

api.add_resource(Store, "/store/<name>")
api.add_resource(Item, "/item/<name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(debug=True)
