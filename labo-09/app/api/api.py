from flask import Blueprint, jsonify, render_template, request, session, url_for
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from schemas.User import User, UserSchema
from schemas.subscribe_schema import subscribe_schema
from shared import db, schema, mail
import urllib3
import xmltodict

# from child import child
api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

def generate_token(email):
    safe = URLSafeTimedSerializer('mysecret')
    return safe.dumps(email)

def confirm_token(token, expiration=3600):
    safe = URLSafeTimedSerializer('mysecret')
    try:
        email = safe.loads(token, max_age=expiration)
    except:
        return False
    return email

# api_v1.register_blueprint(child)
@api_v1.route('/users')
def all_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    serialized_users = user_schema.dump(users)
    return jsonify({'users': serialized_users})

@api_v1.route('/user/new', methods=['POST'])
def create_user():
    data = request.get_json();
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'todo'}), 201

@api_v1.route('/inscription', methods=['POST'])
@schema.validate(subscribe_schema)
def inscription():
    data = request.get_json()

    token = generate_token(data['email'])
    message = Message("Courriel d'activation", sender="mmasson.inf5190@gmail.com", recipients=data['email'])
    message.body = f'''
    Pour activer votre compte cliquez ici :
     {url_for('router.activer_email', token=token)}
    '''

    # mail.send(message)

    return {"message": "User subscribed"}, 200

@api_v1.route('/data')
def get_patinoire():
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml')
    try:
        data = xmltodict.parse(response.data)
    except:
        print("Failed to parse xml from response (%s)" %
              traceback.format_exc())
    return jsonify({"data": data})

