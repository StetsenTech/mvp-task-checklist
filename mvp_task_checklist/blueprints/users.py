from flask import Blueprint, jsonify, make_response, request

from ..components import UserComponent

users = Blueprint('users', __name__, url_prefix='/users')


@users.route('/', methods=['GET'])
def get_users():
    """Gets a list of all users in the system

    Return:
        Response containing an array of all user dictionareis
    """
    return make_response(jsonify(data=UserComponent.get_users()), 200)

@users.route('/', methods=['POST'])
def create_user():
    """Creates a new user
    """
    request_data = request.get_json()
    return make_response(
        jsonify(UserComponent.create_user(request_data)), 200
    )

@users.route('/<user_id>', methods=['GET'])
def get_user(user_id:int):
    """Returns a list of all users
    
    Arguments:
        user_id {int} -- ID of user to query information for
    
    Return:
        Resposne containing a users information
    """
    return make_response(jsonify(UserComponent.get_user(user_id)), 200)

@users.route('/<user_id>/tasks', methods=['GET'])
def get_user_tasks(user_id:int):
    """Returns a list of all tasks for users
    
    Arguments:
        user_id {int} -- ID of user to query data for
    
    Return:
        Resposne containing a list of users tasks
    """
    pass
