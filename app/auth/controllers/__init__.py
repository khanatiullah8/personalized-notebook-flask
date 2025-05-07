from flask import Blueprint
from flask_restful import Api
from app.auth.controllers.signup import SignupView

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

api = Api(auth_blueprint)

api.add_resource(SignupView, '/signup')