#Dictionary
student={
    'name': 'anjal',
    'age' : 23,
    'place' : 'malappuram'
}

print(student)
print(len(student))

print(student['age'])
a=student.get('age')
print(a)

print(student.keys())  #print keys of dictionary
print(student.values()) #print values of dictionary
print(student.items()) #priint both keys and values of dictionary

stud=dict(name='aa',age=25,place='Calicut')
print(stud)
print(type(stud))

if 'age' in student:
    print('present')

student['age']=30  #change values of dictionary
print(student)

student.update({'name':'Anjal Muhammed M A'})
print(student)

student.update({'phone':7591901980 })
print(student)

