# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 08:49:58 2022

@author: LXA20
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        
        print(self.time)
        
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
   
    def __eq__(self, other):
        # First make sure `other` is of the same type 
        assert type(other) == type(self)
        return ((self.x == other.x) and (self.y == other.y))
   
    

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'

