list1=[12,-7,5,64,-14]
list2=[]

for i in list1:
    if i > 0:
        list2.append(i)
    else:
        print("this is negative number")

print(list2)