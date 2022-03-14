# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:16:30 2022

@author: LXA20
"""

def oddTuples(aTup):
    '''
    

    Parameters
    ----------
    aTup : a tuple
        returns every other element of aTup

    Returns
    -------
    tuple

    '''
    oddTup = ();
    for i in range(len(aTup)):
        #Since indexing starts at 1, the zeroeth element is on add element
        if  i%2 ==0: 
            oddTup = oddTup + (aTup[i],)
    return oddTup

aTup = ('I', 'am', 'a', 'test', 'tuple')    
newTup = oddTuples(aTup)



