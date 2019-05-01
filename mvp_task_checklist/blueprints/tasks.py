from flask import Blueprint, request, make_response, jsonify
from flask_login import login_required

from ..components import TaskComponent
tasks = Blueprint('tasks', __name__, url_prefix='/tasks')


@tasks.route("/")
def get_tasks():
    """Gets tasks for current task
    """
    return make_response(jsonify(data=TaskComponent.get_tasks()), 200)

@tasks.route('/', methods=['POST'])
def create_task():
    """Creates a new task
    """
    request_data = request.get_json()
    return make_response(
        jsonify(TaskComponent.create_task(request_data)), 200
    )

@tasks.route('/<task_id>')
def get_task(task_id:int):
    """Gets a specific task
    
    Arguments:
        task_id {int} -- ID of task to get information about
    """
    return make_response(jsonify(TaskComponent.get_task(task_id)), 200)
