#odd even
number=[1,2,3,4,5,6,7,8,9,10]
oddno=[]
evenno=[]

for i in range (len(number)):
    if (number[i]%2==0):
        evenno.append(number[i])
    else:
        oddno.append(number[i])

print("Even Numbers are : " , evenno)
print("Odd Numbers are : " , oddno)