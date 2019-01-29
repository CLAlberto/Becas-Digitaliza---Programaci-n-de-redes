#Familiarize the student with:

#projecting and writing parameterized functions;
#utilizing the return statement;
#building a set of utility functions;
#utilizing her/his own functions.
#Scenario
#Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

#Use the previously written and tested functions. Add some test cases to the code. Our test is only a beginning.



def IsYearLeap(year):
		if year % 4 == 0 and year % 100 != 0:
			print("El año", year, "es bisiesto")
			return True
		elif year % 400 == 0:
			print("El año", year, "es bisiesto")
			return  True
		else:
			print("El año", year, "NO es bisiesto")
			return  False
def DaysInMonth(year,month):

		if month == 1:
			print("el mes ", month,"del año ",year,"tiene 31 días")
		elif month == 3:
			print("el mes ", month, "del año ", year, "tiene 31 días")
		elif month == 4:
			print("el mes ", month, "del año ", year, "tiene 30 días")
		elif month == 5:
			print("el mes ", month, "del año ", year, "tiene 31 días")
		elif month == 6:
			print("el mes ", month, "del año ", year, "tiene 30 días")
		elif month == 7:
			print("el mes ", month, "del año ", year, "tiene 31 días")
		elif month == 8:
			print("el mes ", month, "del año ", year, "tiene 31 días")
		elif month == 9:
			print("el mes ", month, "del año ", year, "tiene 30 días")
		elif month == 10:
			print("el mes ", month, "del año ", year, "tiene 31 días")
		elif month == 11:
			print("el mes ", month, "del año ", year, "tiene 30 días")
		elif month == 12:
			print("el mes ", month, "del año ", year, "tiene 31 días")
		elif month == 2:
			if IsYearLeap(year):
				print("el mes ", month, "del año ", year, "tiene 29 días")
			else:
				print("el mes ", month, "del año ", year, "tiene 28 días")
		else:
			print("Por favor, introduce un mes válido")

def DayOfYear(year,month,day):
    for m in range(month):
        if month <5:
            dayofyear = ((month - 1) * 31) + day
        elif month <6:
            dayofyear = ((month - 1) * 31) + day - 1
        elif month <9:
            dayofyear = ((month - 1) * 31) + day - 2
        elif month <10:
            dayofyear = ((month - 1) * 31) + day - 3
        else:
            dayofyear = ((month - 1) * 31) + day - 4

    if  month >2:
        if IsYearLeap(year):
            dayofyear = dayofyear - 2
        else:
            dayofyear = dayofyear - 3
    else:
        dayofyear
    print("el día",day, "del mes",month, "del año",year,"equivale al día número",dayofyear,"de todos los dias que tiene el año",year)
    return int(dayofyear)





DayOfYear(int(input("Introduce el año: ")),int(input("Introduce el mes: ")),int(input("Introduce el dia: ")))   