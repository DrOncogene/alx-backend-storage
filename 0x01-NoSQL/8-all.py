#!/usr/bin/env python3
"""
list all document in a collecion
"""


def list_all(mongo_collection):
    """list all documents"""
    return mongo_collection.find()
