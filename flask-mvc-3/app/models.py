# class User:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#
#     def __str__(self):
#         return f'name: {self.name} - age: {self.age} - city: {self.city}'
#
#     def __repr__(self):
#         return str(self.__dict__)

from app import db


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(20), nullable=False)
    pets = db.relationship('Pet', backref='user', cascade='all, delete', lazy=True)

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f'name: {self.name} - age: {self.age} - city: {self.city}'

    def __repr__(self):
        return str(self.__dict__)
