import datetime

date_of_birth = input("\nEnter your date of birth (e.g. 04/07/2006): ").split("/")

day_of_birth = int(date_of_birth[0])
month_of_birth = int(date_of_birth[1])
year_of_birth = int(date_of_birth[2])

current_date = (datetime.datetime.now().strftime("%d/%m/%Y")).split("/")

current_day = int(current_date[0])
current_month = int(current_date[1])
current_year = int(current_date[2])

this_year_age = current_year - year_of_birth

if current_month < month_of_birth or (current_month == month_of_birth and current_day < day_of_birth):
    print(f"Since it hasn't been her birthday yet, her age is {this_year_age - 1}.\n")
elif current_day == day_of_birth and current_month == month_of_birth:
    print(f"Happy Birthday! Today is {current_day}/{current_month:02}/{current_year}, your birthday, and your age is {this_year_age}.\n")
else:
    print(f"Since your birthday has already passed, your age is X. {this_year_age}.\n")
