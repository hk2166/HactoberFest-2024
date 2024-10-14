from datetime import datetime

def find_age(current_date, current_month, current_year, birth_date, birth_month, birth_year):
    # Create datetime objects for the current date and birth date
    current_date_obj = datetime(current_year, current_month, current_date)
    birth_date_obj = datetime(birth_year, birth_month, birth_date)

    # Calculate the age
    age = current_date_obj - birth_date_obj

    # Convert the age to years, months, and days
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30

    # Print the age
    print("Present Age")
    print("Years:", years, "Months:", months, "Days:", days)

# Driver code
current_date = int(input("Enter current date (dd): "))
current_month = int(input("Enter current month (mm): "))
current_year = int(input("Enter current year (yyyy): "))

birth_date = int(input("Enter birth date (dd): "))
birth_month = int(input("Enter birth month (mm): "))
birth_year = int(input("Enter birth year (yyyy): "))

find_age(current_date, current_month, current_year, birth_date, birth_month, birth_year)
