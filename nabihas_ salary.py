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
}
while(month == ""):
    month =  input("You can't enter nothing: ")
if month != "":
    for x,y in months_dict.items():
        if month == x or month.capitalize()==y:
            month = y