def lowestPayment(balance, annualInterestRate, minFixedPayment):
    
    '''
    Will calculate the lowest payment that will pay off debt in one year!
    Float balance - the outstanding balance on the credit card 
    Float: annualInterestRate - annual interest rate
    Float: monthlyPaymentRate - minimum monthly payment rate 
    
    '''
    # monthlyInterestRate = (annualInterestRate/12);
   
    balance = balance - minFixedPayment;
  
    balance = balance + monthlyInterestRate*balance;

    return balance;

initBalance = 320000;

roundBalance = initBalance;

balance = initBalance;

annualinterestRate = 0.2;
monthlyInterestRate = (annualinterestRate/12);


month = 1;
# Set tolerance
Tol = 0.001

lower = balance/12;
upper = balance*(1+ monthlyInterestRate)**12/12;
minFixedPayment = lower + (upper-lower)/2;
# print('upper: ' +str(upper) + ' lower: ' + str(lower))

while abs(roundBalance)> 0 and (upper-lower)/2 > Tol:
    minFixedPayment = (lower + (upper-lower)/2);
    if roundBalance >= 0:
        while month <= 12:
            balance = lowestPayment(balance, monthlyInterestRate, minFixedPayment)
            roundBalance = round(balance, 2)
            # print('Month:' + str(month) + ' Remaining balance: '+str(roundBalance));
            month +=1; 
        month = 1;
        lower = lower + .01;
        # print('Payment too low balance: ' + str(balance) + ' minFixedPayment: ' + str(minFixedPayment))
        # print('upper: ' +str(upper) + ' lower: ' + str(lower))
        balance = initBalance;
        roundPayment = round(minFixedPayment, 2)
        
    elif roundBalance <= 0:
        while month <= 12:
            balance = lowestPayment(balance, monthlyInterestRate, minFixedPayment)
            roundBalance = round(balance, 2)
            # print('Month:' + str(month) + ' Remaining balance: '+str(roundBalance));
            month +=1;
        
        month = 1;
        upper = upper - 0.01;
        # print('Payment Too high: balance: ' + str(balance) + ' minFixedPayment: ' + str(minFixedPayment))
        # print('upper: ' +str(upper) + ' lower: ' + str(lower))
        balance = initBalance;
        roundPayment = round(minFixedPayment, 2)
    

print('Lowest Payment: ' + str(roundPayment))  