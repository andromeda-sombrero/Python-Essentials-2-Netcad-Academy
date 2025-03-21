"""
Lab Exercise 6 - Points on a Plane

Each point located on the plane can be described as a pair of coordinates
customarily called x and y. We want you to write a Python class which stores
both coordinates as float numbers. Moreover, we want the objects of this class
to evaluate the distances between any of the two points situated on the plane.

The task is rather easy if you employ the function named hypot()
(available through the math module) which evaluates the length of the
hypotenuse of a right triangle.

This is how we imagine the class:

it's called Point;

its constructor accepts two arguments (x and y respectively), both of which
default to zero; all the properties should be private;

the class contains two parameterless methods called getx() and gety(), which
return each of the two coordinates (the coordinates are stored privately, so
they cannot be accessed directly from within the object);

the class provides a method called distance_from_xy(x,y), which calculates and
returns the distance between the point stored inside the object and the other
point given as a pair of floats;

the class provides a method called distance_from_point(point), which calculates
the distance (like the previous method), but the other point's location is
given as another Point class object;
"""


import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        #
        # Write code here
        #

    def getx(self):
        #
        # Write code here
        #

    def gety(self):
        #
        # Write code here
        #

    def distance_from_xy(self, x, y):
        #
        # Write code here
        #

    def distance_from_point(self, point):
        #
        # Write code here
        #


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
    