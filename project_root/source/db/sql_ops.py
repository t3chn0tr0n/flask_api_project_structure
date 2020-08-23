import sqlalchemy as db
from sqlalchemy import Column
from sqlalchemy.orm import Session

from . import config

DB_URI = "".join([
    config.SQL_DB_TYPE,
    "://",
    config.SQL_DB_USER,
    ":",
    config.SQL_PASSWORD,
    "@",
    config.SQL_DB_HOST,
    ":",
    str(config.SQL_SQL_DB_PORT),
    "/",
    config.SQL_DATABASE])


class Database():
    engine = db.create_engine(DB_URI)

    def __init__(self):
        self.connection = self.engine.connect()

    def save(self, modelObj):
        session = Session(bind=self.connection)
        session.add(modelObj)
        session.commit()

    def get(self, model_obj, pk=None):
        self.session = Session(bind=self.connection)
        if pk is None:
            data = self.session.query(model_obj).all()
        else:
            data = self.session.query(model_obj).filter(
                model_obj.id == pk,
                model_obj.active == True
            )
        arr = []
        for t in data:
            del t.__dict__['_sa_instance_state']
            arr.append(t.__dict__)
        return arr

    def fetch(self, model_obj, keys):
        self.session = Session(bind=self.connection)
        data = self.session.query(model_obj).filter_by(**keys)
        arr = []
        for t in data:
            del t.__dict__['_sa_instance_state']
            arr.append(t.__dict__)
        return arr

    def fetchByQuery(self, query: str):
        fetchQuery = self.connection.execute(query)
        return [x for x in fetchQuery.fetchall()]

    def update(self, model_obj, pk, data_to_update):
        self.session = Session(bind=self.connection)
        data = self.session.query(model_obj).filter(
            model_obj.id == pk
        )
        data.update(data_to_update)
        self.session.commit()

    def delete(self, model_obj, pk):
        self.session = Session(bind=self.connection)
        self.session.query(model_obj).filter(
            model_obj.id == pk).delete()
        self.session.commit()
