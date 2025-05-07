from flask import request
from flask_restful import Resource
from app.auth.models import User
from app.auth.serde import user_schema
from app import db

class SignupView(Resource):
  def post(self):
    req = request.get_json()
    data = user_schema.load(req)
    
    user_exist = User.query.filter_by(username=data["username"]).count()
    
    if user_exist:
      return {"message":"username already taken"}, 409
    
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    
    return {"message": "signup successful"}, 201
  
    