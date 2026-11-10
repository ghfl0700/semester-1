# Week 1.6, Session 1: Task 1

import math


class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        if not isinstance(x, int):
            raise TypeError("x coordinate must be an integer")

        if not isinstance(y, int):
            raise TypeError("y coordinate must be an integer")

        self.x = x
        self.y = y

    def distance(self):
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, other):
        """
        Returns distance of this Point from another Point.
        """

        dx = self.x - other.x
        dy = self .y - other.y
        return math.hypot(dx, dy)

a = Point(0, 0)
b = Point(3, 4)
print(a.distance_to(b))