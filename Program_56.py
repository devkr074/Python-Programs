# for Loops in Python

print(f"\nUsing for Loop\n")
fruits=["Apple","Banana","Cherry"]
for x in fruits:
    print(x)
print(f"\nLooping Through a String\n")
for x in "Banana":
    print(x)
print(f"\nUsing break Statement in for Loop\n")
for x in fruits:
    print(x)
    if x=="Banana":
        break
print(f"\nUsing continue Statement in for Loop\n")
for x in fruits:
    if x=="Banana":
        continue
    print(x)
print(f"\nUsing range Function\n")
for x in range(6):
    print(x)
print(f"\nUsing Start Parameter in range Function\n")
for x in range(2,6):
    print(x)
print(f"\nUsing Increment Parameter in range Function\n")
for x in range(2,30,3):
    print(x)
print(f"\nUsing else Statement in for Loop\n")
for x in range(6):
    print(x)
else:
    print("Finally finished!")
print(f"\nNested for Loop\n")
adj=["Red","Big","Tasty"]
fruits=["Apple","Banana","Cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
print(f"\nUsing pass Statement\n")
for x in [0,1,2]:
    pass