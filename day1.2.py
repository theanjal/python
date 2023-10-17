#search in string
name='Anjal Muhammed M A'
print(name[2])
print(len(name))

d='I am, Anjal Muhammed M A'
print('Anjal' in d)
print('Asheel' in d)

#slicing
print(d[2:4])
print(d[:5])

#upper case and lower case
print(d.upper())
print(d.lower())

#strip - to remove the first white space
a=' students'
print(a.strip())

#replace letters
print(a.replace ('s','a'))

#split a string
print(d.split(","))

#concatination of strings
b='Anjal'
c='Muahmmed'
print(b + " " +c)

#boolean
e=10<20
f=1>4
print(e)
print(f)

print(bool ())

#arithmetic operations
x=10
y=20
m=y-x
n=x+y
o=x*y
p=x/y

print(m)
print(n)
print(o)
print(p)

print(50+20*3)