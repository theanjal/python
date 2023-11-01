#Tuple packing , unpacking
animal=('cat','dog','deer')
(x,y,z)=animal
print(x)
print(y)
print(z)

animals=('cat','dog','deer')
(x,*y)=animals
print(x)
print(y)

animalss=('cat','dog','deer','fox','pig')
(x,*y,z)=animalss
print(x)
print(y)
print(z)

birds=('crow','parrot','eagle')

#join two tuples
c=animal+birds
print(c)

#count
a=(1,2,3,4,1,5,6)
b=a.count(1)
print(b)

#index value
c=a.index(2)
print(c)

#slicing
print(birds[:])
print(birds[1:2])