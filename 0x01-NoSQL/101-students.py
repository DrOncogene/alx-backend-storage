#!/usr/bin/env python3
"""
aggregating results
"""


def top_students(mongo_coll):
    """sort by average scores"""
    match = mongo_coll.aggregate([
      {'$set': {'averageScore': {'$avg': '$topics.score'}}},
      {'$sort': {'averageScore': -1}}
    ])
    return match
