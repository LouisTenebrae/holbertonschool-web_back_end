#!/usr/bin/env python3
'''Change school topics'''


def update_topics(mongo_collection, name, topics):
    '''Updates the topics for a given school'''
    if mongo_collection is None:
        return None
    else:
        mongo_collection.update_many(
            {"name": name}, {"$set": {"topics": topics}})
        return None
