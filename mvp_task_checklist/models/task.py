from peewee import (
    BooleanField, CharField, ForeignKeyField, TextField
)

from .base import BaseModel
from .user import User
from .project import Project

class Task(BaseModel):
    """Model for Tasks table"""
    name = CharField(null=False)
    desc = TextField()
    user = ForeignKeyField(User, backref='created_tasks', null=False)
    project = ForeignKeyField(Project, backref='tasks', null=False)
    assignee = ForeignKeyField(User, backref='assigned_tasks')
    is_completed = BooleanField(default=False)
    parent = ForeignKeyField('self', null=True, backref='children')
