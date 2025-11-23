#area adn perimetre of rectangle
l = int(input("enter a lenght "))
b = int (input("enter breath "))
area = l*b
peri = 2*(l+b)
print("area is ",area,"perimetre is ",peri)


#is even or odd

n = int(input("enter  a number"))
if(n&1==0):
    print("even")
else:
    print("oddd")

# area and volume of cube

l = int(input("enter a lenght "))
area = 6*l*l
volume = l**3
print("area is ",area,"volume is ",volume)

# equation

x = int(input("enter a number"))
y = int (input("enter a number"))
z= (x**2)-(y**2)
print(z)

#another equation
z=(x**2)+(y**2)
print(z)

#convert celsius to ferhenit

c = float(input("enter temp in celsius"))
f=((9/5)*c)+32
print(f)
