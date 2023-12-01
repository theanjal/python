#file handling

#f=open("notes.txt") #open file
#f=open("notes.txt","rt")

f=open("notes.txt","r")
print(f.read())
print(f.read(3))
print(f.readline())
print(f.readline())

#print using loop
for x in f:
    print(x)



#write- append mode

f=open("notes2.txt","a")
f.write('Hai anjal')
f.close()

f=open("notes2.txt","r")
print(f.read())


#write -over write

f=open("notes2.txt","w")
f.write('Hello world!')
f.close()

f=open("notes2.txt","r")
print(f.read())




#delete file
import os

if os.path.exists("notes2.txt"):
    os.remove("notes2.txt")
else:
    print("File not found!")

#delete folder
os.rmdir("folder") #delete empty folder

#create file

f=open("notes2.txt","x")