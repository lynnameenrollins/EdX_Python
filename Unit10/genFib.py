# -*- coding: utf-8 -*-
"""
Created on Thu May 19 08:44:36 2016

@author: ericgrimson
"""

def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
        
      
def genPrimesLynn():
    '''
    returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

    '''
    primes = [2]
    x=2
       
    while True:
        i=0
        #check to see if a number is prime by checking if it is divisible by each number in the list of primes
        for n in primes:
            
            #print("n in primes, n:" +str(n))
            if x % primes[i] !=0:
                i += 1
                test = True;
            else:
                #if a number is divisible then it is not a prime, break out of the loop
                test = False
                break;
        if test:
            #append the number to the list, stop on next, go on to the next number
            primes.append(x)
            next = primes 
            yield next
            x +=1
        else:
            #the number is not a prime number, add one and check again
            x +=1
            
            
# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html 

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

        
