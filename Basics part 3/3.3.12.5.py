#A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers. In the USA it is shown as the number of miles travelled by car using one gallon of fuel.

#Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

#The functions:

#are named l100kmtompg and mpgtol100km respectively;
#take one argument (the value corresponding to their names)
#Complete the code presented below.

#Run your code and check whether your output is the same as ours.

#Well, you will surely need this:

#1 American mile = 1609.344 metres;
#1 American gallon = 3.785411784 litres.



def l100kmtompg(litres):
    mpg = (378.5411784 / litres) / 1.609344
    return mpg


def mpgtol100km(miles):
    km = miles * 1.609344
    kml = (100 * 3.785411784) / km
    return kml


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))