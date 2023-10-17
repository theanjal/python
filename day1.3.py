#list
fruits=['mango','banana','jackfruit','apple','orange']
print(fruits)
print(len(fruits))
print(type(fruits))

print(fruits[1])
print(fruits[1:])
print(fruits[:4])
print(fruits[2:4])

print('pappaya' in fruits)

fruits[0:1]=['pappaya','grapes']
print(fruits)

#insert to list
fruits.insert(2, 'cherry')
print(fruits)

#append
fruits.append('mango')
print(fruits)

birds=['parrot','crow', 'eagle','peacok']

fruits.extend(birds)
print(fruits)