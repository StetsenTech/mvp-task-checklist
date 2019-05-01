import json

from playhouse.shortcuts import model_to_dict, dict_to_model

from ..models import User


class UserComponent():
    """Module that handles logic for users"""

    def create_user(user_data:dict) -> dict:
        """Creates a new user
        
        Arguments:
            user_data {dict} -- Data to used to create new user
        
        Returns:
            dict --  Data of newly created user
        """
        user = dict_to_model(User, user_data)
        user.save()

        return model_to_dict(user)

    def get_users() -> list:
        """Gets a set of users
        
        Returns:
            list[dict] -- List of user data
        """
        users = User.get_all()
        
        excludes = [User.password]
        return [model_to_dict(user, recurse=False, exclude=excludes) for user in users]

    def get_user(user_id:int) -> dict:
        """Gets a user 
        
        Arguments:
            user_id {int} -- ID of user
        
        Returns:
            dict -- Data for the user
        """
        user = User.get_by_id(user_id)

        excludes = [User.password]
        return model_to_dict(user, backrefs=True, exclude=excludes, max_depth=1)
