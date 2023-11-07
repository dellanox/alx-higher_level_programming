#!/usr/bin/python3
"""Defines an object attribute and its  methods using lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes and methods."""
    return (dir(obj))
