# Unpacking a Tuple in Python

fruits=("Apple","Banana","Cherry")
print(fruits)
(Green,Yellow,Red)=fruits
print(Green)
print(Yellow)
print(Red)
fruits=("Apple","Banana","Cherry","Strawberry","Raspberry")
print(fruits)
(Green,Yellow,*Red)=fruits
print(Green)
print(Yellow)
print(Red)