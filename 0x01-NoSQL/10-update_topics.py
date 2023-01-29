#!usr/bin/env python3
"""
updates a record
"""
from pymongo.collection import Collection


def update_topics(mongo_coll: Collection, name, topics):
    """updates a mongo document"""
    match = mongo_coll.find_one({"name": name})
    if match is None:
        mongo_coll.insert_one({'name': name, 'topics': topics})
    else:
        mongo_coll.update_one({"name": name}, {'$set': {"topics": topics}})
