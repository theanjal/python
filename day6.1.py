#set
x={1,2,3,4}
print(x)
print(len(x))
print(type(x))

#covert tuple to set
a=(1,2,3,4,6,6)
b=set(a)
print(b)
print(type(a))
print(type(b))

#print
for i in x:
    print(i)

#add
x.add(10)
print(x)

#update
y={11,22,33}
x.update(y)
print(x)

#remove
x.remove(33)
print(x)

x.discard(33)  #no error with already deleted element
print(x)

x.discard(22)
print(x)

'''
x.remove(33) #will be error
print(x)
'''

