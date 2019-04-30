from peewee import CharField, DateField, ForeignKeyField, TextField

from .base import BaseModel
from .user import User

class Project(BaseModel):
    """Model for the Projects table"""
    name = CharField()
    desc = TextField()
    user = ForeignKeyField(User, backref='projects', null=False)
    created = DateField()
    modified = DateField()
