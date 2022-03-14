# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 14:22:42 2022

@author: LXA20
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:

        item/= denom
    except ZeroDivisionError:
        item = 0
            
    return item
 
 