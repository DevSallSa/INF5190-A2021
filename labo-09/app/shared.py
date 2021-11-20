from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail
from flask_json_schema import JsonSchema

mail = Mail()
db = SQLAlchemy()
ma = Marshmallow()
schema = JsonSchema()
