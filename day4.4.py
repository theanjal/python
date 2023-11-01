#Tuple square, cube
a=(1,2,3,4,5,6,7)
for i in range(len(a)-1):
    srq=a[i]*a[i]
    cub=a[i]*a[i]*a[i]
    print(a[i])
    print("square is :",srq)
    print("Cube is :",cub)