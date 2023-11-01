#set 

a={1,2,3,4,5}
b={4,5,6,7,8}
print(a)
print(b)
#union
c=a.union(b)
print(c)

#intersection
d=a.intersection(b)
print(d)

#difference
e=a.difference(b)
print(e)

f=a.difference_update(b)
print(f)

x={'banana','pappaya','apple','orange'}
y={'potato','banana','chilly'}

print(x)
print(y)

x.difference_update(y)
print(x)

x.intersection_update(y)
print(x)