import json

from playhouse.shortcuts import model_to_dict, dict_to_model

from ..models import Task


class TaskComponent():
    """Module that handles logic for tasks"""

    def create_task(task_data:dict) -> dict:
        """Creates a new task
        
        Arguments:
            task_data {dict} -- Data to used to create new task
        
        Returns:
            dict --  Data of newly created task
        """
        task = dict_to_model(Task, task_data)
        task.save()

        return model_to_dict(task)

    def get_tasks() -> list:
        """Gets a set of tasks
        
        Returns:
            list[dict] -- List of task data
        """
        tasks = Task.get_all()

        return [model_to_dict(task, recurse=False) for task in tasks]

    def get_task(task_id:int) -> dict:
        """Gets a task 
        
        Arguments:
            task_id {int} -- ID of task
        
        Returns:
            dict -- Data for the task
        """
        task = Task.get_by_id(task_id)

        return model_to_dict(task, backrefs=True, max_depth=1)
