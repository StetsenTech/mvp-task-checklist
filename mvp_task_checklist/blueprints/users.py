from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/users', methods=['GET'])
def get_users():
    """Gets a list of all users in the system

    Return:
        Response containing an array of all user dictionareis
    """
    pass

@users.route('/users/', methods=['POST'])
def create_user():
    """Creates a new user
    """
    pass

@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id:int):
    """Returns a list of all users
    
    Arguments:
        user_id {int} -- ID of user to get information for
    
    Return:
        Resposne containing a users information
    """
    pass

@users.route('/users/<user_id>/tasks', methods=['GET'])
def get_user_tasks(user_id:int):
    """Returns a list of all tasks for users
    
    Arguments:
        user_id {int} -- ID of user to get information for
    
    Return:
        Resposne containing a list of users tasks
    """
    pass
