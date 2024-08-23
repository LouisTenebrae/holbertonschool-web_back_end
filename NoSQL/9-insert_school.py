#!/usr/bin/env python3
'''Insert a document in Python'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document into a MongoDB collection'''
    if mongo_collection is None:
        return None
    else:
        return mongo_collection.insert_one(kwargs).inserted_id
