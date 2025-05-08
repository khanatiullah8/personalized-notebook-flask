from flask import Blueprint
from flask_restful import Api
from app.auth.controllers.signup import SignupView
from app.auth.controllers.login import LoginView
from app.auth.controllers.logout import LogoutView

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

api = Api(auth_blueprint)

api.add_resource(SignupView, '/signup')
api.add_resource(LoginView, '/login')
api.add_resource(LogoutView, '/logout')