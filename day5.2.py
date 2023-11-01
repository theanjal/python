#Dictionary merge
fruits={
    'apple':{
        'price':100,
        'color':'red'
    },
    'orange':{
        'price':70,
        'color':'orange'
    },
    'grape':{
        'price':90,
        'color':'green'
    }
}


#duplicate deletion in dictionary

studentdata={
    'id1':{
        'name':'sara',
        'class':5,
        'subject':'maths, science, social'
    },
    'id2':{
        'name':'surya',
        'class':5,
        'subject':'maths, science, social'
    },
    'id3':{
        'name':'sara',
        'class':5,
        'subject':'maths, science, social'
    },
    'id4':{
        'name':'surya',
        'class':5,
        'subject':'maths, science, social'
    },
}

student={}
for key,value in studentdata.items():
    if value not in student.values():
        student[key]=value
print(student)

