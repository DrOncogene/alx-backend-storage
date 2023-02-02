#!/usr/bin/env python3
"""
creates a Cache class
"""
from uuid import uuid4
from functools import wraps
from typing import Union, Optional, Any, Callable

import redis


def count_calls(method: Callable) -> Callable:
    """
    count and store the number of
    times a method is called
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(*args, **kwargs):
        self = args[0]
        self._redis.incr(key, 1)
        return method(*args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    persist method call history
    in a list in redis
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(*args, **kwargs):
        self = args[0]
        self._redis.rpush(f'{key}:inputs', str(args[1:]))
        output = method(*args, **kwargs)
        self._redis.rpush(f'{key}:outputs', str(output))
        return method
    return wrapper


class Cache():
    """convenience wrapper around redi-py"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores data"""
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """gets a value from redis db"""
        value = self._redis.get(key)
        if fn is not None:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """use get but with a str func argument"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """use get with int func"""
        return self.get(key, int)
