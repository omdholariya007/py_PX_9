# counting number of times occurence

t1 = (1,2,3,4,5,6)
x= int(input("enter your number"))
c=0
for i in t1:
    if(i==x):
        c=c+1
print(c)

# is in tuple
t1 = (1,2,3,4,5,6)
x= int(input("enter your number"))
for i in t1:
    if(i==x):
        print ("yes it exist ")
        break

#tuple to string
t1 = (1,2,3,4,5,6)
str1 = ""
for i in t1:
    str1= str1 + str(i)

print(str1)

# max and min in tuple
t1 = (1,2,3,4,5,6)
print("maximum is ",max(t1),"minimum is",min(t1))

# tuple of sring to string
t1 =('sb','fo','ko','si')
str1=""
for i in t1:
    str1=str1+i
print(str1)

# sorting tuple of integers
t3 = (4,6,1,54,41,40,13,14)
l3=list(t3)
l3.sort()
t3 = tuple(l3)
print(t3)

# first and last output

t3 = (4,6,1,54,41,40,13,14)
l2 = list(t3)
print("first is ",l2[0],"lst is ", l2[-1])
      
