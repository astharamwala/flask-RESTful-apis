import logging
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from security import authentication, identify
from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList

from db import db



logger = logging.getLogger("ENV OF LOGGER")

logger.debug("Flask app starts now")
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDatabase.db'

api = Api(app)
app.secret_key = "SomeSecretKey"

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app, authentication, identify)

api.add_resource(Store,"/store/<name>")
api.add_resource(Item, "/item/<name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, '/register')


app.run(debug=True)
