#!/usr/bin/env python3
"""
creates a Cache class
"""
from uuid import uuid4
from typing import Union

import redis


class Cache():
    """"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores data"""
        key = str(uuid4())
        self._redis.set(key, data)

        return key
