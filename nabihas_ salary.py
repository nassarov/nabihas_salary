# Finance Summary Program
salary = float(input("Please enter your salary : "))
month =  input("Please enter the name of the month: ")
months_dict = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}
while(month == ""):
    month =  input("You can't enter nothing: ")
if month != "":
    for x,y in months_dict.items():
        if month == x or month.capitalize()==y:
            month = y
            print(f"Month: {month}")
            break #stop when one is found to not print it 2 times 

# get the % from user
print("Please enter percentages for:")
savings_per = float(input("(1) Savings: "))
rent_per = float(input("(2) Rent: "))
electricity_per = float(input("(3) Electricity: "))

# real value
savings = salary*(savings_per/100)
rent = salary*(rent_per/100)
electricity = salary*(electricity_per/100)
# calculations
total = savings + rent +electricity
remainder = salary - total
yearly_rent = 12*rent
yearly_elec = 12*electricity

# fun 
fun = salary**2
# bonus
additional = float(input("Additional amount of money for this month: "))
remaining = additional - additional*(savings_per/100)
total_saving = savings + remaining


# RESULTS:
print("##############################")
print(f"Summary of {month}: ")
print("##############################")
print(f"Salary : ${salary}")
print(f"->Rent : ${rent}")
print(f"->Electricity : ${electricity}")
print(f"->Savings : ${savings}")
print("---------------------------")
print(f"Total Expenses : ${total}")
print(f"Remaining Salary : ${remainder}")
print("##############################")
print("YEARLY APPARTMENT EXPENSES : ")
print(f"->Yearly Rent : ${yearly_rent}")
print(f"->Yearly Electricity : ${yearly_elec}")
print("---------------------------")
print(f"Total : ${yearly_elec+yearly_rent}")
print("##############################")
print(f"Just for fun (Salary^2) : {fun}")
print("##############################")
print(f"Your Additional Savings : ${additional}")
print(f"Remaining from Additional Savings : ${remaining}")
print("---------------------------")
print(f"Total Savings With Additional Money : ${total_saving}")