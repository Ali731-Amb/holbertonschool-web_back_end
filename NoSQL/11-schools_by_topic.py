#!/usr/bin/env python3
"""Module that returns schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        list of school documents that have the topic
    """
    return list(mongo_collection.find({"topics": topic}))
