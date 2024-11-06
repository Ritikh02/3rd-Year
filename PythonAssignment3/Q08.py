# Question 8: Write a Python program that takes the name of a month as input and returns the number of days in that month.
# Input: The name of the Month: February
# Output: No. of days: 28/29 days

def days_in_month(month):
    month_days = {
        "January": 31, "February": "28/29", "March": 31,
        "April": 30, "May": 31, "June": 30,
        "July": 31, "August": 31, "September": 30,
        "October": 31, "November": 30, "December": 31
    }
    return month_days.get(month, "Invalid month name")

user_month = input("Enter the name of the month: ")
print(days_in_month(user_month))
