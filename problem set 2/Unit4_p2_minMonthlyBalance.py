# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 06:23:02 2022

@author: LXA20
"""
import math


def lowestPayment(balance, annualInterestRate, minFixedPayment):
    
    '''
    Will calculate the lowest payment that will pay off debt in one year!
    Float balance - the outstanding balance on the credit card 
    Float: annualInterestRate - annual interest rate
    Float: monthlyPaymentRate - minimum monthly payment rate 
    
    '''
    monthlyInterestRate = (annualInterestRate/12);
   
    balance = balance - minFixedPayment;
  
    balance = balance + monthlyInterestRate*balance;

    return balance;

initBalance = 3926;

roundBalance = initBalance;

balance = initBalance;
interestRate = 0.2;
minFixedPayment = 0;
month = 1;

while roundBalance >= 0:
    minFixedPayment += 10;
    while month <= 12:
        balance = lowestPayment(balance, interestRate, minFixedPayment)
        roundBalance = round(balance, 2)
        # print('Month:' + str(month) + ' Remaining balance: '+str(roundBalance));
        month +=1;
    
    month = 1;
    balance = initBalance;
    

print('Lowest Payment: ' + str(minFixedPayment))        
