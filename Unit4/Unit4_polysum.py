# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 20:54:09 2022

@author: LXA20
"""

import math

def polysum(n,s):
    
    area = (0.25*n*s**2)/math.tan(math.pi/n);
    perimeter = n*s;
    
    sum = area + perimeter**2;
    return round(sum, 4)


print(polysum(4,5))