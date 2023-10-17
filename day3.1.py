#list comprehension
subject=['english','malayalam','tamil','physics','chemistry']
sub=[i for i in subject if 's' in i]
print(sub)        

#without list comprehension
for i in range (len(subject)):
    if 's' in subject[i]:
        sub.append(subject[i])
print(sub)        

