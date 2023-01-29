#!/usr/bin/env python3
"""
computes nginx log stats
saved in a mongodb
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # connect to the db
    client = MongoClient('mongodb://127.0.0.1:27017')
    # get the collection reference
    nginx_logs = client.logs.nginx

    # number of documents
    all_entries = len(list(nginx_logs.find()))
    # number of GET requests
    n_get = len(list(nginx_logs.find({'method': 'GET'})))
    # POST requests
    n_post = len(list(nginx_logs.find({'method': 'POST'})))
    # PUT requests
    n_put = len(list(nginx_logs.find({'method': 'PUT'})))
    n_patch = len(list(nginx_logs.find({'method': 'PATCH'})))
    n_delete = len(list(nginx_logs.find({'method': 'DELETE'})))
    # number of status checks
    n_statuses = len(list(nginx_logs.find({'method': 'GET', 'path': '/status'})))

    print(f'{all_entries} logs')
    print('Methods:')
    print(f'\tmethod GET: {n_get}')
    print(f'\tmethod POST: {n_post}')
    print(f'\tmethod PUT: {n_put}')
    print(f'\tmethod PATCH: {n_patch}')
    print(f'\tmethod DELETE: {n_delete}')
    print(f'{n_statuses} status check')
