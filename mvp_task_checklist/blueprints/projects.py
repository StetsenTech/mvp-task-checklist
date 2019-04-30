from flask import Blueprint

projects = Blueprint('projects', __name__)

@projects.route('/projects/', methods=['GET'])
def get_projects():
    """Gets a list of all projects

    Return:
        List of all projects available
    """
    pass


@projects.route('/projects/', methods=['POST'])
def create_project():
    """Creates a new project
    """
    pass

@projects.route('/projects/<project_id>')
def get_project(project_id:int):
    """Gets a specific project
    
    Arguments:
        project_id {int} -- ID of project to get information for
    """
    pass

@projects.route('/projects/<project_id>/tasks')
def get_project_tasks(project_id:int):
    """Gets all tasks for a specific project
    
    Arguments:
        project_id {int} -- ID of project to get tasks for
    """
    pass
