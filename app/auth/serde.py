from marshmallow import fields, Schema

class UserSchema(Schema):
  id = fields.Int(dump_only=True)
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(load_only=True)
  
  
user_schema = UserSchema()
users_schema = UserSchema(many=True)