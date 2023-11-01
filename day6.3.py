#set sub-set
a={1,2,3,4,5,6,7,8}
b={2,3,7,4}

c=a.issubset(b)
print(c)

d=b.issubset(a)
print(d)

e=a.issuperset(b)
print(e)

print(max(a)) #max
print(min(a)) #min

if 3 in a:
    print('present')