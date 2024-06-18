"""
Zubair Islam
ZI23110011984

T05 - Capstone Project - Variables and Control Structures

1.User is presented with a print out describing two options to choose
2.User inputs bond or investment, regardless of caps/case. 
If other than that is inputed, then print Invalid Input
IF ELIF and ELSE statements used for options

3.For bond option, user prompted to input 
houseValue (converted to integer), 
interestRate (converted to float) 
and numberOfMonths (converted to integer)
4. Repayment is calculated & then printed to user.

5. For investment option, user prompted to input;
depositAmount (converted into integer),
interestRate (converted into float),
and numberOfYears (converted into integer)

6. Then user is presented with option of simple or compound
7. User inputs a choice, case insensitive, 
invalid input is captured by else statement

8. Using IF ELIF and ELSE statement, 
if Simple selected then calculation is made accordingly and printed to user
if Compound is selected then calculation is made and printed to user
ELSE captures invalid input

#786
#Completed by Zub1Wun on 2024-06-09 Sunday

from tkinter import *

def calculate_conversion():
    miles = float(miles_input_entry.get())
    km = round(miles*1.609,2)
    conversion_output_label.config(text=f"{km}")


window = Tk()
window.title("Zub1Wun's Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)

#Entry
miles_input_entry = Entry(width=10)
miles_input_entry.grid(column=1, row=0)

#Label
miles_label = Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

#Label
is_equal_to_label = Label(text="is equal to", font=("Arial", 16, "bold"))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

#Label
conversion_output_label = Label(text="0", font=("Arial", 18, "bold"))
conversion_output_label.grid(column=1, row=1)
conversion_output_label.config(padx=10, pady=10)

#Label
km_label = Label(text="Km", font=("Arial", 16, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

#Button
calculate_button = Button(text="Calculate", command=calculate_conversion)
calculate_button.grid(column=1, row=2)


window.mainloop()

"""

import math

# display options and sentence explaining them
# prompt user to choose an option
print("""\n---------------------------------------------------------------------------------------
\tinvestment\t- to calculate the amount of interest you'll earn on your investment
\tbond\t\t- to calculate the amount you'll have to pay on a home loan
---------------------------------------------------------------------------------------\n""")

#input choice
#convert to lowercase and then compare to bond and investment
userChoice = input("Enter either 'investment' or 'bond' from the menu above to proceed : ").lower().strip()

#if userChoice is bond
if userChoice=="bond":
    print("\n***bond calculation selected***\n")
    houseValue = int(input("Input the present value of the house : "))

    #accepts floats, so that user can for example input 2.5 as interest
    interestRate = (float(input("Input interest rate : ")))/100/12 ##correction pointed out in review I left out dividing by 12 
    numberOfMonths = int(input("Enter the number of months you plan to take to repay the bond : "))

    repayment = (interestRate*houseValue)/(1-(1+interestRate)**(-numberOfMonths))
    #use round function to round repayment to 2 decimal points
    repayment = round(repayment, 2)
    print(f"\nRepayment : {repayment:,}\n", )
    #PROGRAM ENDS

#elif userChoice is investment    
elif userChoice=="investment":
    print("\n***investment calculation selected***")
    depositAmount = int(input("Input amount of money to deposit : "))

    #accepts floats, so that user can for example input 2.5 as interest
    interestRate = (float(input("Input interest rate as a percentage without %, just the number : ")))/100 
    numberOfYears = int(input("Input the number of years to invest : "))

    interest = input("\nDo you want 'simple' or 'compound' interest? : ").lower().strip()

    if interest=="simple":
        totalAfterInterestApplied = depositAmount *(1 + (interestRate*numberOfYears))
        #use round function to round totalAfterInterestApplied to 2 decimal points
        totalAfterInterestApplied = round(totalAfterInterestApplied, 2)
        print(f"\n{totalAfterInterestApplied:,} is the total amount once the interest has been applied\n")
        #PROGRAM ENDS

    elif interest=="compound":
        totalAfterInterestApplied = depositAmount * math.pow((1+interestRate),numberOfYears)
        #use round function to round totalAfterInterestApplied to 2 decimal points
        totalAfterInterestApplied = round(totalAfterInterestApplied, 2)
        print(f"\n{totalAfterInterestApplied:,} is the total amount once the interest has been applied\n")
        #PROGRAM ENDS

    else:
        print("\nInvalid input\n")
        #PROGRAM ENDS
else:
    print("\nInvalid input\n")
    #PROGRAM ENDS#
