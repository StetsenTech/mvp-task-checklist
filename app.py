from flask import Flask, jsonify, make_response
from flask_login import LoginManager

from mvp_task_checklist.blueprints import projects, users, tasks
from mvp_task_checklist.models import db, User

app = Flask(__name__)
db.connect()

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def status():
    message = {
        'message': 'success'
    }

    return make_response(jsonify(message), 200)

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response


app.register_blueprint(projects)
app.register_blueprint(users)
app.register_blueprint(tasks)