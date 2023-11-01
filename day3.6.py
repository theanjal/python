#list of colors and print last and first element
colors=['red','blue','green','white','black','violet']
print(colors[0])
print(colors[len(colors)-1])

#remove duplicate element from list
color=['red','blue','green','white','black','red','violet']
colors=[]
for i in range(len(color)):
    if color[i] not in colors:
        colors.append(color[i])
print(colors)