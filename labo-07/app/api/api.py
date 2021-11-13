from flask import Blueprint, jsonify, render_template, request, session
# from child import child
api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

# api_v1.register_blueprint(child)
@api_v1.route('/login', methods=["POST"])
def create_session():
    profile = request.get_json()
    session['profile'] = profile
    session['step'] = 1

    return {"message": "success"}, 201


@api_v1.route('/logout')
def logout_user():
    session.pop('profile', None)
    return {"message": "Gracefully gone !"}, 200
