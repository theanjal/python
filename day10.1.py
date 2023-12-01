
import sum
print(sum.myfunc(2,4))


#build in mathematical functions
x=print(min(1,2,3,4,5,6))
x=print(max(1,2,3,4,5,6))
#y=print(ciel(1.22))
#y=print(floor(1.22))
y=print(abs(-99))
y=print(pow(2,3))


import math

print(math.sqrt(3))
print(math.pi)
print(math.radians(60))
print(math.degrees(1))
print(math.sin(60))#cos tan
print(math.factorial(5))



import random

print(random.randint(20,50))
print(random.random())

x=[1,2,3,45,67,8,90]
print(random.choice(x))



import datetime

print(datetime.datetime.now())

x = datetime.datetime(2023,11,28)
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%d"))
print(x.strftime("%D"))