#Dictionary
student={
    'name': 'anjal',
    'age' : 23,
    'place' : 'malappuram'
}


stud=student.copy() #copy
print(stud)

student.pop('age') #pop
print(student)

student.popitem() #popitem
print(student)

student.clear() #clear
print(student)

del(student) #delete
print(student)

