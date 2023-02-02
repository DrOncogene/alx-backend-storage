#!/usr/bin/env python3
"""
fetch and cache pages
in redis
"""
import redis
import requests

db = redis.Redis()


def get_page(url: str) -> str:
    """
    fetch and cache pages
    """
    res = requests.get(url, timeout=1000)
    db.setex(url.removeprefix('http://'), 10, res.text)
    db.incrby(f'count:{url}', 1)

    return res.text
