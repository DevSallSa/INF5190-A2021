from flask import Blueprint

users_api = Blueprint('user_api', __name__)

@users_api.route('/users')
def get_all():
    return {"message": "Get all users"}, 200
