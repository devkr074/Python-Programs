# Looping List in Python

myList=["Apple","Banana","Cherry"]
print(f"\nUsing for Loop\n")
for x in myList:
    print(x)
print(f"\nUsing Index Numbers\n")
for i in range(len(myList)):
    print(myList[i])
print(f"\nUsing while Loop\n")
i=0
while i<len(myList):
    print(myList[i])
    i=i+1
print(f"\nUsing List Comprehension\n")
[print(x) for x in myList]