from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange


class UserForm(Form):
    name = StringField('Name', [DataRequired(), length(2,20, 'name must be 2-20 characters')])
    age = IntegerField('Age', [DataRequired(), NumberRange(18, 120,'age must be 10-120')])
    city = StringField('City', [DataRequired(), length(2,20, 'city must be 2-20 characters')])
    save = SubmitField('Save')