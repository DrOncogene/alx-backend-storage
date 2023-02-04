#!/usr/bin/env python3
"""
fetch and cache pages
in redis
"""
from datetime import timedelta

import redis
import requests

db = redis.Redis()


def get_page(url: str) -> str:
    """
    fetch and cache pages
    """
    res = requests.get(url, timeout=1000)
    db.setex(url, timedelta(seconds=10.0), res.text)
    db.incr(f'count:{url}', 1)

    return res.text
