# problem1_ChristianMills.py

# sets reference year
current_year = 2024
current_month = 12

# get the year and persist if incorrect datatype
while True:
    try:
        year = int(input("Hi there! What year were you born in? "))
        break
    except ValueError:
        print("Whoops! Please input a year in XXXX format...\n")

# get month and persist if incorrect datatype
while True:
    try:
        month = int(input("Awesome! What month were you born in? (1-12) "))
        break
    except ValueError:
        print("Whoops! Please input the number in which month you were born in...\n")

# first calculation (using year)
age = 2024 - year

# second calculation (takes into account month)
age = age - 1 if month > current_month else age

# reveal how horrifically old they are
print(age)