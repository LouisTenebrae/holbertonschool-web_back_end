#!/usr/bin/env python3
'''List all documents in Python'''


def list_all(mongo_collection):
    '''Returns all documents from a MongoDB collection'''
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.find()
