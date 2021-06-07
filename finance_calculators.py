import math 
#provide options for calculations

print("Please type either 'investment' or 'bond' from the menu below to proceed:")
print("")
print("investment   - to calculate the amount of interest you'll earn on interest")
print("bond         - to calculate the amount you'll have to pay on a home loan")
print("")
user_choice = input("Please select (investment or bond): \n")

#adjust how to proceed accordingly(apply adjustments for variations of selection case)

if user_choice == "investment" or user_choice == "Investment" or user_choice == "INVESTMENT":

    p = float(input("Please enter the deposited amount: \n"))
    r_annual = float(input("Please enter the current interest rate(eg: enter 8 and not 8%.): \n"))
    r = (r_annual / 100)
    t = int(input("Please enter the amount of years you intend to invest for: \n"))
    interest = input("Would you like 'compound' or 'simple' interest to be caculated?: \n")

#aquire amounts for variables (variable names mirror represented name in formula provided)  

    if interest == "simple" or interest == "Simple" or interest == "SIMPLE":

        a = p * (1 + r * t)
        a = round(a,2)

        print(f"Your total amount will be R{a}")

#simple interest formula applied and displayed

    elif interest == "compound" or interest == "Compound" or interest == "COMPOUND":

        a = p * math.pow((1 + r),t)
        a = round(a,2)

        print(f"Your total amount will be R{a}")

#compound interest formula applied and displayed

    else:
        print("invalid selection")

#message displayed if 'simple' or 'compound' is not selected 

elif user_choice == "bond" or user_choice == "Bond" or user_choice == "BOND":
    p2 = float(input("What is the value of the house?(E.g. 100000): \n"))
    interest_rate = int(input("What is the current annual interest rate?(E.g 7): \n"))
    i = float(interest_rate / 12)
    n = int(input("how many months do you plan to repay the bond?(E.g 120: \n"))

#aquire amounts for variables (variable names mirror represented name in formula provided)
    
    a2 = (i * p2)/(1 - math.pow((1+i),(-1*n)))
    a2 = round(a2,2)
    
    print(f"your total amount to pay per month wil be {a2}")

#bond formula applied and displayed
    
else:
    print("invalid selection")

#message displayed if 'interest' or 'bond' is not selected
#end
