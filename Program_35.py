# Update Tuple in Python

myTuple=("Apple","Banana","Cherry")
myList=list(myTuple)
myList[1]="Kiwi"
myTuple=tuple(myList)
print(myTuple)
myList.append("Orange")
myTuple=tuple(myList)
print(myTuple)
myList.remove("Apple")
myTuple=tuple(myList)
print(myTuple)
myTuple2=("Pineapple",)
myTuple=myTuple+myTuple2
print(myTuple)