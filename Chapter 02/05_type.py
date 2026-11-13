a = 31 
t = type(a) # Class <int>

print(t) 

b = "zaid" 
t = type(b) # class <str>
print(t)

c = 3.14
t = type(c) # class <float>
print(t)

d = "2.5"
t = type(d) # class <str> because of ("")
print(t)

e = True
t = type(e) # class <boolean>
print(t)

# converting data types

f = 3
i = float(f) # convert the integer 3 to a float 3.0   
t = type(i) # class <float>
print(i)

j = 7.0
i = int(j) # convert the float 7.0 to an integer 7, the decimal part is truncated
t = type(i) # class <int>
print(i)

a = "5"
b = float(a) # convert the string "5" to a float 5.0
t = type(b)
print(t)

a = 2
b = bool(a)
t = type(b)
print(b) # true because any non-zero integer is considered true in boolean context
print(t)

a = 5.9
b = int(a)
c = type(b)
print(b) ,print(c)
