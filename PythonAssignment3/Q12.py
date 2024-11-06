# Question 12: Write a Python program using functions that prompt the user to enter today’s date (in the format YYYY-MM-DD) and the current day of the week. Then, ask the user to input a number of days. The program should calculate and display the new date and the day of the week after the specified number of days have passed.
# Input: Today’s date: 2024-08-27, Today’s day: Tuesday, Number of days: 5
# Output: New date: 2024-09-01, New day: Sunday

from datetime import datetime, timedelta

def calculate_new_date(today_date, today_day, num_days):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_day_index = days_of_week.index(today_day)
    new_day_index = (start_day_index + num_days) % 7
    new_date = datetime.strptime(today_date, "%Y-%m-%d") + timedelta(days=num_days)
    return new_date.strftime("%Y-%m-%d"), days_of_week[new_day_index]

today_date = input("Enter today's date (YYYY-MM-DD): ")
today_day = input("Enter today's day: ")
num_days = int(input("Enter number of days: "))
new_date, new_day = calculate_new_date(today_date, today_day, num_days)
print(f"New date: {new_date}, New day: {new_day}")
