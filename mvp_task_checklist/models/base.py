from peewee import Model, SqliteDatabase
from playhouse.flask_utils import PaginatedQuery


db = SqliteDatabase('mvp-task-checklist.db')

class BaseModel(Model):
    """Base model for tables"""
    class Meta:
        database = db

    @classmethod
    def get_all(cls,limit:int=20,offset:int=1):
        """Querys for all records of a model
        
        Keyword Arguments:
            limit {int} -- Number of records to select (default: {20})
            offset {int} -- Start of records (default: {1})
        
        Returns:
            [type] -- [description]
        """
        return cls.select().limit(limit).offset(offset)

    @classmethod
    def get_by_id(cls, id):
        """Gets a record by id
        
        Arguments:
            id {[type]} -- ID of record on table
        
        Returns:
            [type] -- [description]
        """
        return cls.get(id=id)
