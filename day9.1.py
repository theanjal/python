#arguments:

#arbitary arguments - '*' -*args

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")


#keyword arguments -kwargs

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#arbitary keyword arguments- **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#default parameter

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#pass
def myfunction():
  pass

#can list as argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#lamda function
#lambda arguments : expression

x = lambda a : a + 10 #add
print(x(5))

x= lambda a,b : a*b #multiplication
print(x(5,6))

x= lambda a :a*a*a #cube
print(x(5))


#map 
animals = ['dog', 'cat', 'parrot', 'rabbit']
# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
print(uppered_animals)

#filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list)


#squr-lambda
x=lambda a:a*a
print(x(3))

#list-set of no. greater than 10- filter function
lis = [20,10,9,8,22,43,19,3]
final_lis = list(filter(lambda x : (x>10), lis))
print(final_lis)

#map fuc - lowwr case - list
birds = ['CROW','EAGLE','HEN','PARROT']
birds_low = list(map(lambda x : str.lower(x), birds))
print(birds_low)
