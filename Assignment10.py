def find_leap_years(start_year, num_years):
    leap_years = []
    current_year = start_year
    while len(leap_years) < num_years:
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            leap_years.append(current_year)
        current_year += 1
    return leap_years
start_year = int(input("Enter a starting year : "))
num_years = 15
leap_years_list = find_leap_years(start_year, num_years)
print("The next 15 leap years starting from", start_year, "are : ", leap_years_list)