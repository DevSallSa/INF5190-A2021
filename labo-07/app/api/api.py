from flask import Blueprint, jsonify, render_template
# from child import child
api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

# api_v1.register_blueprint(child)
