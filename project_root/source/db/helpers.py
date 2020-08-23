from sqlalchemy import Column

from .sql_ops import Database


class Model():
    @classmethod
    def create(cls, data: dict):
        """
            Inserts a new data
            :params:
                - data: data to e inserted
            :returns: data as a Class Object
        """
        db = Database()
        data = cls(**data)
        db.save(data)
        return data

    @classmethod
    def update(cls, pk, data: dict):
        """
            Updates a data in a row
            :params:
            - pk: primary key for the table
            - data: New data to be updated
            :returns: None
        """
        db = Database()
        data_to_update = {}
        attrs = cls.__dict__
        for key, value in data.items():
            data_to_update[attrs[key]] = value
        db.update_data(cls, pk, data_to_update)

    @classmethod
    def get(cls, pk):
        """
            :params:
            - pk: primary key for the table
            :returns:
            A list of all found data for a pk. If no pk supplied, all data is returned!
        """
        db = Database()
        data = db.get(cls, pk)
        return data

    @classmethod
    def get_all(cls):
        """
            :params:
            - None
            :returns:
            A list of all data
        """
        db = Database()
        data = db.get(cls)
        return data

    @classmethod
    def fetch(cls, **keys):
        """
            :params:
            - key: to search using data, not pk
            :returns:
            A list of all found data 
        """
        db = Database()
        keys = {}
        data = db.fetch(cls, keys)
        return data

    @classmethod
    def soft_delete(cls, pk):
        """
            Deactivates a field - makes "active=False". 
        """
        db = Database()
        data_to_update = {
            cls.active: False
        }
        db.update(cls, pk, data_to_update)

    @classmethod
    def execute_query(cls, query):
        """
            Executes query (Not specific to this class...can access any query! Therefore, use with caution!)
        """
        db = Database()
        return db.fetchByQuery(cls, query)

    @classmethod
    def delete(cls, pk, soft=False):
        if soft:
            cls.soft_delete(pk)
        db = Database()
        db.delete(cls, pk)