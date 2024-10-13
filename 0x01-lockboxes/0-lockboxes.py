#!/usr/bin/python3
"""
defines the canUnlockAll function that determines if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.
    """

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
