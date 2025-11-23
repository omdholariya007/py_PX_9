import math
# convert degree to radian

d= float(input("enter degree"))
r = math.radians(d)
print("radian is ",r)

# calculate y = 6x^2+4 sinx
x = float(input("enter a number"))
y= 6*(x**2)+(4*(math.sin(math.radians(x))))
print (y)


#calculate
x= int(input("enter a number "))
y = math.radians(x)
fx = math.cos(math.radians(2*x))
print(fx)
print(y)
print(math.sin(22/7))
