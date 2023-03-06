# user chooses between bond or investment calculation
# user capitalisation should not affect outcome e.g investment or INVESTMENT
# if investment, ask user to input:
# amount of money depositing
# inerest rate
# number of years investing
# "simple" or "compound" (stored in variable "interest")
# calculate apporpriate amount they will get back depending on choices and display
# if bond, ask user to input:
# present value of house
# interest rate
# number of months for full repayment of the bond
# calculate monthly repayment display

import math

print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print() # returns whitespace
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print() # returns whitespace
financial_calculator = input("state your choice. ")

if financial_calculator.upper() == "INVESTMENT": # .upper function allows user variance using capitalisation
    deposit = float(input("Enter the amount in pounds that you wish to deposit. £")) # amount deposited
    annual_interest_rate = float(input("Enter interest rate. ")) # current interest rate
    duration = float(input("Enter the number of years you plan to invest. ")) # years planned to invest
    interest = input("Choose either Simple or compound interest. ")
    
    if interest.upper() == "SIMPLE":
        investment1 = deposit*(1 + (annual_interest_rate/100 * duration)) # simple interest formula
        print(f"Under this plan your investment will return £{investment1} in {duration} years.")
    
    elif interest.upper() == "COMPOUND":
        investment2 = deposit * math.pow((1 + annual_interest_rate), duration) # compound interest formula
        print(f"Under this plan your investment will return £{investment2} in {duration} years.")

elif financial_calculator.upper() == "BOND": # .upper function allows user variance using capitalisation
    value_house = float(input("Enter the present value of your house in pounds. £")) # present house value
    annual_interest_rate = float(input("Enter interest rate. ")) # current interest rate
    duration = float(input("Enter the number of months you plan to repay the bond. ")) # number of months planned for repayment
    monthly_interest_rate = annual_interest_rate/12 # computes monthly interest rate
    monthly_repayment = (monthly_interest_rate*value_house)/(1 - (1 + monthly_interest_rate)**(-duration)) # interest formula for monthly bond repayment 
    round_monthly_repayment = round(monthly_repayment, 2) # returns value to two decimal places
    
    print(f"Under this plan your monthly repayments will amount to £{round_monthly_repayment}.")
