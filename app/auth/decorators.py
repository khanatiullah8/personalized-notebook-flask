from functools import wraps
from flask import g, request
import jwt
from app import app

def token_required(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    token = request.cookies.get("token")
    
    if not token:
      return {"message": "token is missing"}, 401
    
    try:
      decoded_token = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
      g.user_id = decoded_token["user_id"]
    except jwt.ExpiredSignatureError:
      return {"message": "token is expired"}, 401
    except jwt.InvalidTokenError:
      return {"message": "invalid token"}, 401
    
    return f(*args, **kwargs)
  return wrapper