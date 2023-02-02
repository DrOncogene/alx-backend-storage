#!/usr/bin/env python3
"""
fetches pages and save stats
in redis
"""
import redis
import requests


def get_page(url: str) -> str:
    """
    fetches pages and compute
    stats
    """
    db = redis.Redis()
    page = requests.get(url, timeout=1000)
    db.setex(url, 10, page.text)
    db.incr(f'count:{url}', 1)

    return page.text
