def leap_year():
    year = int(input("Enter year to check it is leap year or not"))
    if ((year % 400 == 0) | ((year % 4 == 0) & (year % 100 != 0))):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


leap_year()
