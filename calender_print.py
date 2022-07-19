'''Python Quick Codes: Generate the calender of any year.
Using Python in-built module Calendar
'''

import calendar

# Get the year from user
year = int(input("Enter year: "))

# Set first week day of the calender as Monday
calendar.setfirstweekday(calendar.MONDAY)

# Print the calender. m = months in a row.
print(calendar.calendar(year, m=4))
