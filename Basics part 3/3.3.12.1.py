# Your task is to write and test a function which takes one argument (a year) and
# returns True if the year is a leap year, or False otherwise.
# The seed of the function is already sown in the skeleton code (below).

def IsYearLeap(year):

    for e in year:
        if e % 4 == 0 and e % 100 != 0:
            print("El año", e, "es bisiesto")
        elif e % 400 == 0:
            print("El año", e, "es bisiesto")
        else:
            print("El año", e, "NO es bisiesto")

testdata = [1900, 2000, 2016, 1987]
IsYearLeap(testdata)

