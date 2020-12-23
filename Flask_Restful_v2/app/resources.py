from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required

from app.models import UserModel
from app.schemas import UserSchema


class User(Resource):
    @classmethod
    def post(cls):
        candidate = request.get_json()
        error = UserSchema().validate(candidate)
        if error:
            return {'message': error}, 400
        data = UserSchema().load(candidate)

        if UserModel.get_by_email(data['email']):
            return {'message': 'user with this email already exists'}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'user created'}, 201

    @classmethod
    @jwt_required()
    def get(cls, email):
        user = UserModel.get_by_email(email)
        if not user:
            return {'message': 'user is not exists'}, 404
        return UserSchema().dump(user)

    @classmethod
    def delete(cls, email):
        user = UserModel.get_by_email(email)
        if not user:
            return {'message': 'user is not exist'}, 404
        user.delete_from_db()
        return {'message': f'user with email {email} is deleted'}
