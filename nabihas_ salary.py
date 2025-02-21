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
yearly_appartment_expense = 12*(rent+electricity)
# fun 
fun = salary**2
