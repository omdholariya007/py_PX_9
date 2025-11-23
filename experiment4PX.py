#multiply all number in list
l1 = [ 1,2,3,4,5,6,7]
s=1
for i in l1:
    s=s*i
print(s)

# largest number in list

l1 = [ 1,2,3,4,5,6,7]
print(max(l1))

# remove duplicates

l1 = [ 1,2,3,4,5,6,7,5,2,1]
print(list(dict.fromkeys(l1)))


# find common items in 2 list

l1=[1,2,3,4,5,6,7]
l2=[55,8,7,2,45,5]
for i in l1:
    if(i in l2):
        print(i)
