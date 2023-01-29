#!/usr/bin/env python3
"""
select schools by topic
"""


def schools_by_topic(mongo_coll, topic):
    """schools by topic"""
    match = mongo_coll.find({'topics': topic})
    return match
