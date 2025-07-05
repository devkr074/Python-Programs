# Join Lists in Python

list1=["Apple","Mango","Banana"]
list2=[1,2,3]
list3=list1+list2
print(list3)
for x in list2:
    list1.append(x)
print(list1)
list1.extend(list2)
print(list1)