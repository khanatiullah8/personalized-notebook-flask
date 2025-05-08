from marshmallow import fields, Schema

class NoteSchema(Schema):
  id = fields.Int(dump_only=True)
  data = fields.Str()
  created_at = fields.DateTime(dump_only=True)
  user_id = fields.Int()
  
  
note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)