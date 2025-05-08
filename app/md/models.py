from app import db
from datetime import datetime

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)