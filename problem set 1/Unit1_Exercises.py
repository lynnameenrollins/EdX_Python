# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:22:32 2022

@author: LXA20
"""
for i in range(2,12,2):
    print(i)
print('Goodbye')

i = 2
while i<11:
    print(i)
    i += 2
print('Goodbye!')    

i=10
print('Hello!')
while i>1:
    print(i)
    i -= 2
    
end = 6
sum = 0
n=1

while n <= end:
    sum = sum + n
    n += 1
print(sum)

myStr = '6.00x'

for char in myStr:
    print(char)

print('done')
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 

#Unit 1 Problem 1
print("Running Problem 1")
s = 'azcbobobegghakl'
numVowels = 0
for char in s:
        if char == 'a' or char == 'e' or char == 'i' \
           or char == 'o' or char == 'u':
            numVowels += 1
print('Number of vowels: ' + str(numVowels))

#Unit 2 Problem 2
print("Running Problem 2")
numBob = 0

for i in range(len(s)):
    temp = (s[i:(i+3)])
    if temp == 'bob':
        numBob += 1;
    
print('Number of times bob occurs is: ' + str(numBob))

#problem Three
print("Running Problem 3")
s = 'azcbobobegghakl'

#s='abcbcd'

alphastring=""
alphastring += s[0]
for i in range(len(s)-1):
      
    if (s[i])<=(s[i+1]):
        alphastring +=s[i+ 1]
        tempstring = alphastring
    
    else:
        alphastring=s[i+1]
        if len(alphastring)< len(tempstring):
            longestsofar = tempstring
           
        
            
        
print("Longest substring in alphabetical order is: " + longestsofar)