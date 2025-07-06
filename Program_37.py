# Looping Through Tuple in Python

print(f"\nUsing for Loop\n")
fruits=("Apple","Banana","Cherry")
for x in fruits:
    print(x)
print(f"\nUsing Index Number\n")
for i in range(len(fruits)):
    print(fruits[i])
print(f"\nUsing while Loop\n")
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1