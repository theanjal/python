#list
students=['Anjal','Asheel','Baabin','Ebin','Roy','George','Binshad','Hashim','Hisham','Safhal']
print(students)

print(students[:6])
print(students[4:])
print(students[3:5])

print('Safhal' in students)

students[4:6]=['Razeen','Misab']
print(students)

students.insert(2, 'Adnan')
print(students)

students.append('Hanan')
print(students)

school=['Muhammed','Akshay']
students.extend(school)
print(students)