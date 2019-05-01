from peewee import CharField, ForeignKeyField, TextField

from .base import BaseModel
from .user import User

class Project(BaseModel):
    """Model for the Projects table"""
    name = CharField(null=False)
    desc = TextField()
    user = ForeignKeyField(User, backref='created_projects', null=False)
