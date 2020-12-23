from flask_restful import Resource, reqparse, inputs
from app.models import UserModel


class User(Resource):
    req = reqparse.RequestParser()
    req.add_argument('email', required=True, type=str)
    req.add_argument('name', required=True, type=inputs.regex('[A-Za-z]{3,}'), help='only characters and len min 3')

    def post(self):
        data = User.req.parse_args()

        if UserModel.get_by_email(data['email']):
            return {'message': 'user with this email already exists'}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'user created'}, 201

    def get(self, email):
        user = UserModel.get_by_email(email)
        if not user:
            return {'message': 'user is not exists'}, 404
        return user.json()

    def delete(self, email):
        user = UserModel.get_by_email(email)
        if not user:
            return {'message': 'user is not exist'}, 404
        user.delete_from_db()
        return {'message': f'user with email {email} is deleted'}
