#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if not (a + b > c) or not (a + c > b) or not (b + c > a):
        raise TriangleError(AttributeError('The sum of any 2 sides should be larger than the remaining side.'))
    if a == b == c:
        return 'equilateral'
    elif (a == b) | (a == c) | (b == c):
        return 'isosceles'
    else: 
        return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass

