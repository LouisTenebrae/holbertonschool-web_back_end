#!/usr/bin/env python3
'''Where can I learn Python?'''


def schools_by_topic(mongo_collection, topic):
    '''Returns all schools in the database where the given topic is taught'''

    return mongo_collection.find({"topics": topic})
