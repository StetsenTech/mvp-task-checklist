from flask import Blueprint, jsonify, make_response, request

from ..components import ProjectComponent

projects = Blueprint('projects', __name__, url_prefix="/projects")

@projects.route('/', methods=['GET'])
def get_projects():
    """Gets a list of all projects

    Return:
        List of all projects available
    """
    return make_response(jsonify(data=ProjectComponent.get_projects()), 200)


@projects.route('/', methods=['POST'])
def create_project():
    """Creates a new project
    """
    request_data = request.get_json()
    return make_response(
        jsonify(ProjectComponent.create_project(request_data)), 200
    )

@projects.route('/<project_id>')
def get_project(project_id:int):
    """Gets a specific project
    
    Arguments:
        project_id {int} -- ID of project to get information for
    """
    return make_response(jsonify(ProjectComponent.get_project(project_id)), 200)

@projects.route('/<project_id>/tasks')
def get_project_tasks(project_id:int):
    """Gets all tasks for a specific project
    
    Arguments:
        project_id {int} -- ID of project to get tasks for
    """
    pass
