import json

from playhouse.shortcuts import model_to_dict, dict_to_model

from ..models import Project


class ProjectComponent():
    """Module that handles logic for projects"""

    def create_project(project_data:dict) -> dict:
        """Creates a new project
        
        Arguments:
            project_data {dict} -- Data to used to create new project
        
        Returns:
            dict --  Data of newly created project
        """
        project = dict_to_model(Project, project_data)
        project.save()

        return model_to_dict(project)


    def get_projects() -> list:
        """Gets a set of projects
        
        Returns:
            list[dict] -- List of project data
        """
        projects = Project.get_all()
        return [model_to_dict(project, recurse=False) for project in projects]

    def get_project(project_id:int) -> dict:
        """Gets a project 
        
        Arguments:
            project_id {int} -- ID of project
        
        Returns:
            dict -- Data for the project
        """
        project = Project.get_by_id(project_id)
        return model_to_dict(project)
