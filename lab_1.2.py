# Use sep to separate values with a custom character.
print("Hello","python",sep="-")
#Use end to customize what appears at the end of a print() statement.
print("Welcome",end=" ") 
print("Python")

# Create a program that asks the user for their name, age and favourite hobby using the input() function, then display a formatted messge.
name = input("Ener the name: ")
age = int(input("Enter the age: "))
hobby = input("Enter the hobby: ") 
print(f"hello, {name}! At {age}! at {hobby}!")

# add, sub, mul, div, floor div, mod and exponentiation. 
a = int(input("Enter the First Number ")) 
b = int(input("Enter the second Number "))
sum = a+b
sub = a-b
mul = a*b
div = a/b
div1 = a//b
mod = a%b
exp = a**b 
print(sum,sub,mul,div,div1,mod,exp)

#Declares variable datatypes. prit their values and type. 
a = "python"
b = 4.8
c = 5
d = True
e = (5+6j)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))

# Demonstrate logical opertors (and, or, not) 
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)

# Demonstrate assignment operators (=,+=,-=,*=,/=) using  single variable 
a = 5
a+=10
a-=10
a*=10
a/=10
print(a)