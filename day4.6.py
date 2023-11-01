#dictionary
birds={'name':'parrot',\
    'color':'green',
    'price':100}
print(birds)

#print any values, keys, items, values , len, type

#Dictionary
cos={
    'name': 'Asheel',
    'age' : 23,
    'place' : 'calicut'
}

print(cos)
print(len(cos))
print(type(cos))

print(cos['age'])
a=cos.get('age')
print(a)

print(cos.keys()) 
print(cos.values()) 
print(cos.items())


if 'name' in cos:
    print('present')

cos['age']=30 
print(cos)

cos.update({'name':'Anjal Muhammed M A'})
print(cos)