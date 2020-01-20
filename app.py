import logging
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from security import authentication, identify
from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList

logger = logging.getLogger("ENV OF LOGGER")

logger.debug("Flask app starts now")
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDatabase.db'

api = Api(app)
app.secret_key = "SomeSecretKey"

jwt = JWT(app, authentication, identify)

api.add_resource(Store,"/store/<name>")
api.add_resource(Item, "/item/<name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(debug=True)
