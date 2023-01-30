#!/usr/bin/env python3
"""
aggregating results
"""
from pymongo.collection import Collection


def top_students(mongo_coll: Collection):
    """sort by average scores"""
    match = mongo_coll.aggregate([
      {'$set': {'averageScore': {'$avg': '$topics.score'}}}
    ])
    return match
