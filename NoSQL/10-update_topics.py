#!/usr/bin/env python3
"""Module that changes all topics of a school document based on name"""


def update_topics(mongo_collection, name, topics):
    """Change all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to update
        topics (list): list of topics to set

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
