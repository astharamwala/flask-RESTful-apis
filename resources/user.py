import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="This field is required!")
    parser.add_argument("password", type=str, required=True, help="This field is required!")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User already exist!"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

    def get(self):
        return {"Users": [user.json() for user in UserModel.find_all()]}


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_user_id(user_id)
        if user:
            return user.json()
        return {"message":"User Not Found!"}, 404

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_user_id(user_id)
        if user is None:
            return {"message": "User Not Found!"}, 404
        user.delete_from_db()
        return user.json()
