#!/usr/bin/python3
"""
This module contains canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened

    Props:
        boxes is a list of lists
    """

    opened = set([0])  # start with box 0 opened
    keys = set(boxes[0])  # start with the keys in the first box

    while keys:
        new_keys = set()
        for key in keys:
            if key not in opened and key < len(boxes):
                opened.add(key)
                new_keys.update(boxes[key])
        keys = new_keys

    return len(opened) == len(boxes)
