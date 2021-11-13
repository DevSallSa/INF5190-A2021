from flask import Response
from functools import wraps
from flask import session


def authentication_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authenticated(session):
            return send_unauthorized()
        return f(*args, **kwargs)
    return decorated

# Check if the id in in the session flask variable
def is_authenticated(session):
    return "profile" in session

# Only this email has rights for D4 task
def is_admin(email):
    return email == "toto@gmail.com"

def send_unauthorized():
    return Response('Unauthorized', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})
