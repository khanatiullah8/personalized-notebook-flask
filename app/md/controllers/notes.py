from flask import request, g
from app import db
from flask_restful import Resource
from app.auth.decorators import token_required
from app.md.models import Note
from app.md.serde import note_schema, notes_schema

class NoteListView(Resource):
  method_decorators = [token_required]
  
  def post(self):
    req = request.get_json()
    data = note_schema.load(req)
    
    note = Note(**data)
    note.user_id = g.user_id
    
    db.session.add(note)
    db.session.commit()
    
    return {"message":"note added successfully", "data": note_schema.dump(note)}, 201
  
  def get(self):
    notes = Note.query.filter_by(user_id=g.user_id).all()

    return {"message":"note added successfully", "data": notes_schema.dump(notes)}
  

class NoteView(Resource):
  method_decorators = [token_required]
  
  def get(self, note_id):
    note = Note.query.filter_by(id=note_id,user_id=g.user_id).first()
    
    if not note:
      return {"message":"invalid note ID"}
    
    return {"data": note_schema.dump(note)}
  
  def put(self, note_id):
    req = request.get_json()
    data = note_schema.load(req)
    
    note = Note.query.filter_by(id=note_id,user_id=g.user_id).first()
    
    if not note:
      return {"message":"invalid note ID"}
    
    note.data = data["data"]
    db.session.commit()
    
    return {"message":"note updated successfully", "data": note_schema.dump(note)}
  
  def delete(self, note_id):
    note = Note.query.filter_by(id=note_id,user_id=g.user_id).first()
    
    if not note:
      return {"message":"invalid note ID"}
 
    db.session.delete(note)
    db.session.commit()
    
    return {"message":"note deleted successfully"}