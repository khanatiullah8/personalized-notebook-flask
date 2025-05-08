from flask import jsonify, make_response, request
from flask_restful import Resource
from app.auth.models import User
import jwt
from datetime import datetime, timedelta
from app import app

class LoginView(Resource):
  def post(self):
    data = request.get_json()
    
    user_exist = User.query.filter_by(username=data.get("username")).first()
    
    if not user_exist:
      return {"message": "invalid username"}, 401
    
    if not User.verify_password(user_exist, data.get("password")):
      return {"message": "invalid password"}, 401
    
    expire_at = datetime.now() + timedelta(seconds=10)
    
    token = jwt.encode(
      {
        "user_id": user_exist.id,
        "exp": expire_at
      },
      app.config["SECRET_KEY"],
      algorithm="HS256"
    )
    
    response = make_response(jsonify({"message": "login successful"}))
    response.set_cookie('token',token, expires=expire_at, httponly=True)
    
    return response