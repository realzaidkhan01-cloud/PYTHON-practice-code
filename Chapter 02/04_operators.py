# arithmetic operators
a = 10
b = 5
c = a + b # addition
print(c) 


# assignment operators
a = 4-2 # subtraction assignment, assigns in a
print(a)
b = 3
b += 2 # increment the value of b by 2 
print(b)

c = 10
c -= 2 # decrement the value of b by 2 
print(c)


d = 3
d *= 2 # multiply the value of b by 2 
print(d)


e = 4
e /= 2 # divide the value of e by 2 
print(e)

# comparison operators
f = 5<10 # less than operator, returns true if 5 is less than 10
print(f) #True

h = 5>10 # greater than operator, returns true if 5 is greater than 10
print(h) #False

i = 5<=15 # less than or equal to operator returns true if 5 is less than or equal to 15
print(i) #True

j = 5!=10 # not equal to operator returns true if 5 is not equal to 10
print(j) #True

k = 5==5 #equal to operator returns true if 5 is equal to 5
print(k) #True

# logical operators

l = True or False # logical or operator returns true if either of the operands is true
print(l) #True

# Truth table of or, logical and operator code

print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is", False or False)

print("\n\t")
# Truth table of and , logical and operator code

print("True and False is ",True and False)
print("False and True is ",False and True)
print("False and False is ", False and False) 
print("True and True is ",True and True)

print(not(True)) # logical not operator returns true if the operand is True 

print(not(False)) # logical not operator returns true if the operand is false 