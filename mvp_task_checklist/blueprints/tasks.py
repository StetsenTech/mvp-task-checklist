from flask import Blueprint
from flask_login import login_required

tasks = Blueprint('tasks', __name__)


@tasks.route("/tasks/")
@login_required
def get_tasks():
    """Gets tasks for current user
    """
    pass

@tasks.route('/tasks/', methods=['POST'])
def create_task():
    """Creates a new task
    """
    pass

@tasks.route('/tasks/<task_id>')
def get_task(task_id:int):
    """Gets a specific task
    
    Arguments:
        task_id {int} -- ID of task to get information about
    """
    pass