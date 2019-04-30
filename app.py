from flask import Flask, jsonify, make_response
from flask_login import LoginManager

from mvp_task_checklist.blueprints import projects, users, tasks

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def status():
    message = {
        'message': 'success'
    }

    return make_response(jsonify(message), 200)


app.register_blueprint(projects)
app.register_blueprint(users)
app.register_blueprint(tasks)