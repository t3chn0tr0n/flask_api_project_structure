from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError as sste

from . import app, config

DEBUG = config.DEBUG
DB_URI = config.MONGO_DB_URI


def is_db_connectable():
    try:
        db_client = MongoClient(DB_URI, serverSelectionTimeoutMS=200)
        db_client.server_info()
        return True
    except sste:
        return False


def connect_db(database):
    try:
        db_client = MongoClient(DB_URI)
        db = db_client[database]
        return True, db_client, db
    except Exception as e:
        app.logger.error(e)
        return False, None, None


def save_raw(data, database, collection):
    status, db_client, db = connect_db(database)
    if not status:
        return False
    try:
        collection = db[collection]
        x = collection.insert(data)
        if (type(data) is list and len(x) == len(data)) or (type(data) is dict and x is not None):
            return True
        return False
    except Exception as e:
        app.logger.error(e)
        return False
    finally:
        db_client.close()


def delete_raw(query: dict, database: str, collection: str):
    status, db_client, db = connect_db(database)
    if not status:
        return
    try:
        collection = db[collection]
        collection.delete_one(query)
    except Exception as e:
        app.logger.error(e)
    finally:
        db_client.close()


def get_raw(database: str, collection: str, query=None, selection=None, group_by_key="", sort_key="", sort_type=1) -> Union[list, dict]:
    """
        Queries db and returns a list of data from a database and collection
        :params:
            - database: str => database name
            - collection: str => collection name
            - (optional) query: dict => query  
            - (optional) selection: dict => selection ; "_id" added automatically if not present
            - (optional) group_by_key: str => groups data by this key, if present in the data
            - (optional) sort_key => key to sort by (nested keys not handled!)
            - (optional) sort type: int => 1 for asc (default), -1 => desc
        :returns:
            - if no group_by_key present 
                then a list 
            - else 
                a dict
    """
    if selection is None:
        selection = {}
    if query is None:
        query = {}
    status, db_client, db = connect_db(database)
    if not status:
        return {}
    try:
        collection = db[collection]
        if type(query) is not dict or len(query) == 0:
            query = {}
        if type(selection) is not dict or len(selection) == 0:
            selection = {'_id': 0}
        elif "_id" not in selection:
            selection['_id'] = 0

        raw_data = collection.find(query, selection)
        if sort_key:
            raw_data = raw_data.sort(sort_key, sort_type)
        if not group_by_key:
            raw_data = [x for x in raw_data]
            return raw_data

        result = {}
        for x in raw_data:
            key = x.get(group_by_key)
            if not key:
                continue
            if key not in result:
                result[key] = []
            result[key].append(x)
        return result
    except Exception as e:
        raise
        app.logger.error(e)
        return {}
    finally:
        db_client.close()


def update_raw(database: str, collection: str, query: dict, data: dict):
    status, db_client, db = connect_db(database)
    if not status:
        return False
    try:
        collection = db[collection]
        collection.update_one(query, {"$set": data})
        return True
    except Exception as e:
        app.logger.error(e)
        return False
    finally:
        db_client.close()


def getset_auto_counter(database, collection):
    status, db_client, db = connect_db(database)
    if not status:
        return False
    try:
        collection = db[collection]
        if collection.count_documents({}) <= 0:
            collection.insert_one({
                "id": "count",
                "count": 100
            })
            return 100

        val = int([x for x in collection.find(
            {"id": "count"})][-1]['count']) + 1
        select = {
            "id": "count"
        }
        query = {
            "$set": {"count": val}
        }
        collection.update_one(select, query)
        return val
    except Exception as e:
        app.logger.error(e)
        return False
    finally:
        db_client.close()
