# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add distance() method here

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    # Add distance_to() method here

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
    # (This will need a parameter representing another point)

p1 = Point(3, 4)
p2 = Point(1, 2)
print(p1.distance())
print(p1.distance_to(p2))



# Finally, add code here to demonstrate use of Point
