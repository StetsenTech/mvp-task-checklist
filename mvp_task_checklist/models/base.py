from peewee import Model, SqliteDatabase

db = SqliteDatabase('mvp-task-checklist.db')

class BaseModel(Model):
    """Base model for tables"""
    class Meta:
        database = db