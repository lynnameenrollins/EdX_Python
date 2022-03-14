# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 06:42:42 2022

@author: LXA20
"""

#Guess my number exercise
print("Please think of a number between 0 and 100!")

low = 0
high = 100
guess = int((low + high)/2)
good_guess= 0



while good_guess !=1:
    print("Is your secret number " + str(guess) + "?")
    value = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n")

    if value == 'l':
        low = guess;
    elif value == 'h':
        high = guess;
    elif value == 'c':
        print('Game over! Your secret number was: ' + str(guess))
        good_guess = 1;
    else:
        value = input(" Invalid entry. \n Please enter 'h' to indicate the guess is too high. Enter   'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n")

    guess = int((low + high)/2);
  
 

