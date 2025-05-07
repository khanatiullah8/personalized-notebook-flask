from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), nullable=False, unique=True)
  email = db.Column(db.String(100), nullable=False, unique=True)
  _password = db.Column(db.String(256), nullable=False)
  
  @property
  def password(self):
    raise AttributeError("cannot access password")
  
  @password.setter
  def password(self, pwd):
    self._password = generate_password_hash(pwd)
    
  def verify_password(self, pwd):
    return check_password_hash(self._password, pwd)