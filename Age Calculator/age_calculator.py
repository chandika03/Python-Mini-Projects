from datetime import date
def calculate_age(born):
    today = date.today()
    years = today.year - born.year
    months = today.month - born.month
    if today.day < born.day:
        months = months -1 
    if months < 0:
        years -= 1
        months += 12
    return years, months
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
year, month, day = map(int, dob_input.split('-'))
born = date(year, month, day)
years, months = calculate_age(born)
print(f"You are {years} years  and {months} months old.")