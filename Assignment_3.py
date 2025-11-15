#Factorial
import math


def factorial(n):
    if n < 2:
        return 1
    else:
       # print(n, "*")
        return n * (factorial(n-1))
n =int(input("enter the number to which you want Factorial : "))
result = factorial(n)
p = "Facorial of {} is : {}".format(n , result )
print(p)

#Maths module for squreroot

n=int(input("enter the number: "))
from math import  *
print("Squareroot of",n,": ",math.sqrt(n))
from math import  *
print("Logarithm of ",n,": ",math.log(n))
from math import  *
print("Sine of ",n,": ",math.sin(n))