from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    class Meta:
        load_only = ('password',)
    id = fields.Integer()
    email = fields.Email(required=True)
    password = fields.String(validate=Length(8, 200), required=True)
    name = fields.String(validate=Length(2, 20), required=True)

