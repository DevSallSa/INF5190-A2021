from flask import Blueprint, jsonify, render_template, request, session
from schemas.User import User, UserSchema
# from child import child
api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

# api_v1.register_blueprint(child)
@api_v1.route('/users')
def all_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    serialized_users = user_schema.dump(users)
    return jsonify({'users': serialized_users})
