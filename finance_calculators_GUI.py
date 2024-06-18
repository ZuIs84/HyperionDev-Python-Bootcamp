"""#786#
#Zub1Wun#
#Completed by Zub1Wun on 2024-06-09 Sunday



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


#Label
first_label = Label(text="Miles", font=("Arial", 16, "bold"))
first_label.grid(column=2, row=0)
first_label.config(padx=10, pady=10)

"""

import math
from tkinter import *

window = Tk()
window.title("Zub1Wun's Finance Calculator GUI 2024")
window.minsize(width=800, height=600)
window.config(padx=10, pady=10)

def calculate_bond():
    house_value = housevalue_entry.get()
    print(house_value)
    house_value = float(house_value)
    interest_rate = house_value / 100 / 12
    num_of_months = int(months_entry.get())
    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-num_of_months))
    repayment = round(repayment,2)
    repayment_string = f"Repayment : {repayment}"
    label.config(text=repayment_string)

def bond_calculation():
    bond_radiobutton.grid_forget()
    housevalue_label.grid(column=0, row=3)
    housevalue_entry = Entry(width=5)
    housevalue_entry.grid(column=1, row=3)

    months_label.grid(column=0, row=4)
    months_entry = Entry(width=5)
    months_entry.grid(column=1, row=4)

    calculate_button.grid(column=1, row=6)
    print("\n***bond calculation selected***\n")

    label.config(text="Input the present value of the house & number of months")

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)


var = IntVar()

label = Label(text="Select an option below", font=("Arial", 14, "bold"))
label.grid(column=0, row=0)
investment_radiobutton = Radiobutton(text="(1) INVESTMENT - to calculate the amount of interest you'll earn on your investment", variable=var, value=1, command=sel)
investment_radiobutton.grid(column=0, rows=1)
bond_radiobutton = Radiobutton(text="(2) BOND- to calculate the amount you'll have to pay on a home loan", variable=var, value=2, command=bond_calculation)
bond_radiobutton.grid(column=0, rows=2)

# Entry
housevalue_label = Label(text="House Value:", font=("Arial", 14, "bold"))
housevalue_label.grid(column=0, row=3)
housevalue_label.grid_forget()
housevalue_entry = Entry(width=5)
housevalue_entry.grid(column=1, row=3)
housevalue_entry.grid_forget()


# Entry
months_label = Label(text="Months:", font=("Arial", 14, "bold"))
months_label.grid(column=0, row=4)
months_label.grid_forget()
months_entry = Entry(width=5)
months_entry.grid(column=1, row=4)
months_entry.grid_forget()


# Button
calculate_button = Button(text="Calculate", command=calculate_bond)
calculate_button.grid(column=0, row=5)
calculate_button.grid_forget()



window.mainloop()

"""
    print("\n***investment calculation selected***")
    depositAmount = int(input("Input amount of money to deposit : "))

    #accepts floats, so that user can for example input 2.5 as interest
    interestRate = (float(input("Input interest rate as a percentage without %, just the number : "))) / 100
    numberOfYears = int(input("Input the number of years to invest : "))

    interest = input("\nDo you want 'simple' or 'compound' interest? : ").lower().strip()

    if interest == "simple":
        totalAfterInterestApplied = depositAmount * (1 + (interestRate * numberOfYears))
        #use round function to round totalAfterInterestApplied to 2 decimal points
        totalAfterInterestApplied = round(totalAfterInterestApplied, 2)
        print(f"\n{totalAfterInterestApplied:,} is the total amount once the interest has been applied\n")
        #PROGRAM ENDS

    elif interest == "compound":
        totalAfterInterestApplied = depositAmount * math.pow((1 + interestRate), numberOfYears)
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
    
"""
