# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 19:38:50 2022

@author: LXA20
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    testValue = min(a,b);
    while a % testValue !=0 or b % testValue !=0:
        testValue -= 1;
    return testValue;

   
def gcdRecur(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    while b!= 0:
        t = b;
        b = a % b;
        a = t;
    return a;
    
 
'''
print(gcdIter(9, 12))
print(gcdRecur(9, 12))