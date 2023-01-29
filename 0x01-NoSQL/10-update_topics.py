#!/usr/bin/env python3
"""
updates a record
"""


def update_topics(mongo_coll, name, topics):
    """updates a mongo document"""
    mongo_coll.update_one({"name": name}, {'$set': {"topics": topics}})
