# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 06:23:02 2022

@author: LXA20
"""
import math

def getDebt(balance, annualInterestRate, monthlyPaymentRate):
    
    '''
    Will calculate a statement on montly payment and remaining balance to a decimal place.
    Float balance - the outstanding balance on the credit card 
    Float: annualInterestRate - annual interest rate
    Float: monthlyPaymentRate - minimum monthly payment rate 
    
    '''
    monthlyInterestRate = (annualInterestRate/12);
    minMonthlyPayment = monthlyPaymentRate * balance;
        
    balance = balance - minMonthlyPayment;
    balance = balance + monthlyInterestRate*balance;
    return balance;


balance = 484;
interestRate = 0.2;
paymentRate = 0.04;
month = 1;

while month< 13:
    balance = getDebt(balance, interestRate, paymentRate)
    roundBalance = round(balance, 2)
    print('Month:'+ str(month) + ' Remaining balance: '+ str(roundBalance));
    month +=1;

