from flask import Flask, jsonify, make_response
from flask_login import LoginManager, login_required

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def status():
    message = {
        'message': 'success'
    }

    return make_response(jsonify(message), 200)

@app.route('/users', methods=['GET'])
def get_users():
    """Gets a list of all users in the system

    Return:
        Response containing an array of all user dictionareis
    """
    pass

@app.route('/users/', methods=['POST'])
def create_user():
    """Creates a new user
    """
    pass

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id:int):
    """Returns a list of all users
    
    Arguments:
        user_id {int} -- ID of user to get information for
    
    Return:
        Resposne containing a users information
    """
    pass

@app.route('/users/<user_id>/tasks', methods=['GET'])
def get_user_tasks(user_id:int):
    """Returns a list of all tasks for users
    
    Arguments:
        user_id {int} -- ID of user to get information for
    
    Return:
        Resposne containing a list of users tasks
    """
    pass

@app.route('/projects/', methods=['GET'])
def get_projects():
    """Gets a list of all projects

    Return:
        List of all projects available
    """
    pass


@app.route('/projects/', methods=['POST'])
def create_project():
    """Creates a new project
    """
    pass

@app.route('/projects/<project_id>')
def get_project(project_id:int):
    """Gets a specific project
    
    Arguments:
        project_id {int} -- ID of project to get information for
    """
    pass

@app.route('/projects/<project_id>/tasks')
def get_project_tasks(project_id:int):
    """Gets all tasks for a specific project
    
    Arguments:
        project_id {int} -- ID of project to get tasks for
    """
    pass

@app.route("/tasks/")
@login_required
def get_tasks():
    """Gets tasks for current user
    """
    pass

@app.route('/tasks/', methods=['POST'])
def create_task():
    """Creates a new task
    """
    pass

@app.route('/tasks/<task_id>')
def get_task(task_id:int):
    """Gets a specific task
    
    Arguments:
        task_id {int} -- ID of task to get information about
    """
    pass