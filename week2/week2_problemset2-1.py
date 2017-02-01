#! /usr/bin/python


balance = 55
annualInterestRate = 0.12
monthlyPaymentRate = 0.04
total_paid = 0

for i in range(0, 12):
    #print("Month: %s" % i)
    mmp = balance * monthlyPaymentRate
    #print("Minimum monthly payment: %s" % round(minimum_monthly_payment, 2))
    running_balance = (balance - mmp) * (1 + annualInterestRate / 12)
    #print("Running balance: %s" % round(running_balance, 2))
    balance = running_balance
    total_paid += mmp

#print("Total paid: %s" % round(total_paid, 2))
print("Remaining balance: %s" % round(balance, 2))

