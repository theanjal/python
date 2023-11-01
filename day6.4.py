#calculator
a=int(input('enter a number:\n'))
b=int(input('enter another number:\n'))

op=input('Enter the operator:\n')

if op=='+':
    c=a+b
    print(c)
elif op=='-':
    c=a-b
    print(c)
elif op=='*':
    c=a*b
    print(c)
elif op=='/':
    c=a/b
    print(c)
else:
    print('wrong operator!') 