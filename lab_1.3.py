#demonstrate the use of type casting constructors
#Take the input from the user with string. 
# Convert string into an int, float and bool 
# Print values and types 
a = input("Enter the name: ") 
b = int(a) 
c = float(a) 
d = bool(a) 
print(a)
print(type(a)) 
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))  

# Convert this number into an integer using int() and print both with a message explaining the difference.
a = float(input("Enter the decimal number: ")) 
b = int(a) 
print(b) 
print("Difference:")
print("Floating-point number can contain decimal values,")
print("while Integer number contains only whole numbers.") 

# Convert boolean to an integer and a string and print all three values 
a = bool(input("Enter the value of n: "))
b = int(a) 
c = str(b)
print(a,b,c)

# Declare a variable of each datatype
# Print the value, type and memry address 
a = 10 
print(a)
print(type(a)) 
print(id(a)) 
b = 1.3
print(b)
print(type(b)) 
print(id(b)) 
c = "abc"
print(c)
print(type(c)) 
print(id(c))
d = True
print(d)
print(type(d)) 
print(id(d)) 
e = [1,2,3,4,5] 
print(e)
print(type(e)) 
print(id(e)) 
f = (1,2,3,4,5) 
print(f) 
print(type(f)) 
print(id(f))      
g = {a:1,b:2,c:3} 
print(g) 
print(type(g)) 
print(id(g)) 

# Declares two variables with same value 
# print their id memory and check if they are the same. 
# modifies one of the variables and checks the memory address again. 
id1 = 10
id2 = 10
print(id(id1)) 
print(id(id2)) 
print("Checks Memory address = ",(id1 == id2))
idn = 12 
print(id(idn)) 
print(id(id2))
print("Checks New Memory address = ",(idn == id2))