"""
Lab Exercise 7 - Triangle

Now we're going to embed the Point class (see Lab 3.4.1.14) inside another
class. Also, we're going to put three points into one class, which will let
us define a triangle. How can we do it?

The new class will be called Triangle and this is what we want:

the constructor accepts three arguments – all of them are objects of the
Point class;
the points are stored inside the object as a private list;
the class provides a parameterless method called perimeter(),
which calculates the perimeter of the triangle described by the three points;
the perimeter is the sum of all the lengths of the legs (we mention this for
the record, although we are sure that you know it perfectly yourself.)
"""

import math


class Point:
    #
    # The code copied from the previous lab.
    #


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        #
        # Write code here
        #

    def perimeter(self):
        #
        # Write code here
        #


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
    