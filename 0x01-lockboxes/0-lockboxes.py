#!/usr/bin/python3
"""Determine if all boxes have key"""


def canUnlockAll(boxes):
    """Return a true or false if key"""
    lenofBox = len(boxes)
    visited = [False] * lenofBox
    visited[0] = True
    queue = [0]
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < lenofBox and not visited[key]:
                visited[key] = True
                queue.append(key)
    return all(visited)
