# To put a value in the terminal
x = input("x: ")
print(x)

# Modulus
y = 10 % 3
print(y)

f = int(2.5)
print(f)

pi = 3.14
print(type(pi))

# Exponential (e)
ln = 1.6e3
print(ln)

hn = 1.6e-3
print(hn)

round(3.76)
print(round(3.76))

# Complex numbers
z = 3 + 7j
print(z.real)
print(z.imag)

z2 = 4 - 6j
print(z + z2)
print(z * z2)
print(z2 / z)

# indexing
food = "tangArine"
a = food[2:6]
print(type(food))
print(a)

# This particular indexing skips x-1 characters
# each time (::x) where x is a number

# i . e
b = food[::2]
# In this case x = 2 therefore the spacing between each character
#  printed is 2-1 = 1(ommiting or skipping 1 character each time)
# starting from the second character,0, [1], 2, [3], 4, [5] etc.
# From the function food (tangArine)
# we skip 1 character each time = t,n,A,i and e

#Another example this time (::3) therefore 3-1 = 2(ommiting or skipping 2 characters each time)
pool = "today is the day we feast"
print(pool[::3])
# Formatting
name = "Tobi"
age = 29
formatted = f"{name} is {age} years old"
print(formatted) 

# Camel casing and Snake casing
# firstName    and first_name

matric_no = "07086875"
score = 81
grade = "A"
fudge = f"{matric_no}-{score}-{grade}"
print(fudge) 

# Display Forms
table = "Welcome  to the world!"
print(table.upper())
print(table.lower())
print(table.title())

# Creating Lists
empty_list = []
num_list = [1,2,3,4,5]
mixed_list = [1,"bbljz",3.14,True]
print(empty_list,num_list,mixed_list)
print(mixed_list[-2])
# This kind of listing which involves [x:y:z] ;
# y = THE LAST CHARACTER, exclusively 
# x = 1ST CHAR POSITION and 
# z = This particular indexing skips {z-1} characters each time (:z) where z is a number
print(mixed_list[0:3:2])
#this example prints 1 and 3.14 because 
# y = 3, exclusively
# x = 0,
# z = 2;
# Therefore the steps; z = 2 - 1, z = 1, no. of steps skipped = 1

# to add a new character to the list
mixed_list.append(6)
print(mixed_list)
 
# to insert a new character into the list
mixed_list.insert(34,False)
print(mixed_list)

# to remove a character in the list
mixed_list.remove(3.14)
print(mixed_list)

# pop() fuction makes use of the index position of the character for removing it
mixed_list.pop(3)
print(mixed_list)

# TO CREATE RANGE
# similar to indexing (x, y, z) ;
# y = THE LAST CHARACTER, exclusively 
# x = 1ST CHAR POSITION and 
# z =  This value shows how many skips {z-1} characters each time (:z)
rang1 = range(0,10,1)
print(rang1)

# to list the range use function: list()
# y = 10, exclusively
# x = 0,
# z = 1; Therefore the steps; z = 1 - 1, z = 0, no. of steps skipped = 0
list_from_range = list(rang1)
print(list_from_range)


# Membership Test(whether or not the value suggested is in the list or not)
#  which will be printed as either True or False
# using function: (in)
is_in_range = 5 in rang1
is_not_in_range = 15 in rang1

print(is_in_range)
print(is_not_in_range)