#reversing string

s = input("enter a string")
s1 = s[::-1]
print(s1)

#is it palidrome or not

p = input("enter word")
p1=p[::-1]
if(p==p1):
    print("its palidrome")
else:
    print("its not")

#c.Write a Python program to check if a string contains only digits.
d = input("enter a string")
print(d.isdigit())

# longest word in sentence

g=""
s= input("enter a sentence")
word = s.split()
for w in word:
    if(len(w)>len(g)):
        g=w
    else:
        w=w
print(w)

#lenght of the last word in sentence

st = input("enter a srring")
for i in st.split():
    leng = len(i)
print(leng)
