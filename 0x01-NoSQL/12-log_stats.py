#!/usr/bin/env python3
"""
computes log stats
"""
from pymongo import MongoClient
from pymongo.collection import Collection


client = MongoClient('mongodb://127.0.0.1:27017')
nginx_logs: Collection = client.logs.nginx

all_entries = len(list(nginx_logs.find()))
n_get = len(list(nginx_logs.find({'method': 'GET'})))
n_post = len(list(nginx_logs.find({'method': 'POST'})))
n_put = len(list(nginx_logs.find({'method': 'PUT'})))
n_patch = len(list(nginx_logs.find({'method': 'PATCH'})))
n_delete = len(list(nginx_logs.find({'method': 'DELETE'})))
n_statuses = len(list(nginx_logs.find({'method': 'GET', 'path': '/status'})))

print(f'{all_entries} logs')
print('Methods:')
print(f'\tmethod GET: {n_get}')
print(f'\tmethod POST: {n_post}')
print(f'\tmethod PUT: {n_put}')
print(f'\tmethod PATCH: {n_patch}')
print(f'\tmethod DELETE: {n_delete}')
print(f'{n_statuses} status check')
