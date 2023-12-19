#!/usr/bin/env python3
""" Inserts a document in Python"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ Inserts  document into a collection
    based on kwargs
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
