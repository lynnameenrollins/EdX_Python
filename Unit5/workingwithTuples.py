# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:23:42 2022

@author: LXA20

"""

#lecture 6, finger exercise
#how many

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0;
    
    keys = aDict.keys()
    for k in keys:
        items = aDict.get(k)
        count += len(items)

    return count

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated       with it
    '''
    biggest_key = None
    maxCount = 0;
    
    for key in aDict.keys():
        if len(aDict[key])>= maxCount:
            biggest_key = key
            maxCount = len(aDict[key])
    return biggest_key
            
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['c'].append('cat')
animals['c'].append('cow')
animals['c'].append('crow')
print(how_many(animals))

print(biggest(animals))