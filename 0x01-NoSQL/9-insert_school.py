#!/usr/bin/env python3
"""
insert a new document
"""


def insert_school(mongo_coll, **kwargs):
    """inserts a new document"""
    new_id = mongo_coll.insert_one(kwargs).inserted_id
    return str(new_id)
