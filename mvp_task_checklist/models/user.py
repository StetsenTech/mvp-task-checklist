import datetime

from peewee import CharField, DateField
from peewee_extra_fields import SimplePasswordField,EmailField

from .base import BaseModel

class User(BaseModel):
    """Model for the Users table"""
    name = CharField(null=False)
    email = EmailField(null=False)
    password = SimplePasswordField(salt='test', null=False)
    created = DateField(default=datetime.datetime.now)
    modified = DateField(default=datetime.datetime.now)

    @classmethod
    def get_by_email(cls, email:str):
        return cls.get(email=email)