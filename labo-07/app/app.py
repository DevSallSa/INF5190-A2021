from flask import Flask, request, g
from api.api import api_v1
from routes.router import router

import os

app = Flask(__name__, static_folder="static", static_url_path="/")
env_config = os.getenv("ENVIRONMENT")
app.config.from_object(env_config)

app.register_blueprint(api_v1)
app.register_blueprint(router)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database

# Close the connection to the DB
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()

@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(error):
    if request.path.startswith("/api/"):
        return jsonify(error=str(error)), error.code
    else:
        return error

if "__main__" == __name__:
    app.run()
