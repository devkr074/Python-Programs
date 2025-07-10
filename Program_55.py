# while Loop in Python

print(f"\nUsing while Loop\n")
i=1
while i<6:
    print(i)
    i+=1
print(f"\nUsing break Statement in while Loop\n")
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
print(f"\nUsing continue Statement in while Loop\n")
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
print(f"\nUsing else Statement in while Loop\n")
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")