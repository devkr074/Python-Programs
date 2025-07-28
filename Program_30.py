# Sort List in Python

myList=["Orange","Mango","Kiwi","Pineapple","Banana"]
myList.sort()
print(myList)
myList=["Orange","Mango","Kiwi","Pineapple","Banana"]
myList.sort(reverse=True)
print(myList)
def myfunc(n):
  return abs(n-50)
myList=[100,50,65,82,23]
myList.sort(key=myfunc)
print(myList)
myList=["banana","Orange","Kiwi","cherry"]
myList.sort()
print(myList)
myList=["banana","Orange","Kiwi","cherry"]
myList.sort(key=str.lower)
print(myList)
myList=["banana","Orange","Kiwi","cherry"]
myList.reverse()
print(myList)