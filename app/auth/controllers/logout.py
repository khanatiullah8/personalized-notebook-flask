from flask import g, jsonify, make_response
from flask_restful import Resource
from app.auth.decorators import token_required

class LogoutView(Resource):
  
  @token_required
  def get(self):
    response = make_response(jsonify({"message": "logout successful"}))
    response.delete_cookie('token')
    
    return response