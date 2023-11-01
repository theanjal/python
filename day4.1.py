#Tuple
a=(1,4,2,33,55,66)
print(len(a))
print(a[0])
print(a[len(a)-1])
print(a[:4])

if 2 in a:
    print('Value present')

#convert to list
b=list(a)
print(b)

b[2]=22
c=tuple(b) #convert to tuple

print(c)

b.append(100) #append
d=tuple(b)
print(d)

b.remove(66) #remove
e=tuple(b)
print(e)

del(e)  #delete
print(e)

