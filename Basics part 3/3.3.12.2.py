#Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given month/year pair (yes, we know that only February is sensitive to the year value, but we want our function to be universal). The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

#Of course, you can (to be honest: you should!) use the previously written and tested function. It may be very helpful (we cannot say anything more, sorry). We encourage you to use a list filled with the months' lengths. You can create it inside the function - this trick will significantly shorten the code.

#We've prepared a testing code. Expand it to include more test cases.

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


testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]

DaysInMonth(input("Introduce el mes: "),input("Introduce el año: "))