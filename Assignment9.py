day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if is_leap_year(year):
    days_in_month[2] = 29
if day == 31 and month == 12:
    next_day = 1
    next_month = 1
    next_year = year + 1
else:
    if day == days_in_month[month]:
        next_day = 1
        next_month = month + 1
    else:
        next_day = day + 1
        next_month = month
    next_year = year
print(next_day, "-", next_month, "-", next_year)