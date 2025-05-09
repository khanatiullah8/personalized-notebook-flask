from flask import Blueprint
from flask_restful import Api
from app.md.controllers.notes import NoteListView, NoteView

md_blueprint = Blueprint("md", __name__, url_prefix="/md")

api = Api(md_blueprint)

api.add_resource(NoteListView, "/notes")
api.add_resource(NoteView, "/notes/<int:note_id>")