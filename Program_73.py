# String Formatting in Python

print(f"\nF-Strings\n")
txt=f"The price is 49 dollars"
print(txt)
print(f"\nPlaceholders and Modifiers\n")
price=59
txt=f"The price is {price} dollars"
print(txt)
txt=f"The price is {price:.2f} dollars"
print(txt)
txt=f"The price is {95:.2f} dollars"
print(txt)
price=59000
txt=f"The price is {price:,} dollars"
print(txt)
txt="The price is {} dollars"
print(txt.format(price))
qty=3
itemNo=567
myOrder="I want {} pieces of item number {} for {:.2f} dollars"
print(myOrder.format(qty,itemNo,price))
myOrder="I want {1} pieces of item number {0} for {2:.2f} dollars"
print(myOrder.format(qty,itemNo,price))
myOrder="I have a {carname}, it is a {model}"
print(myOrder.format(carname="Ford",model="Mustang"))
print(f"\nOperations in F-Strings\n")
txt=f"The price is {20*59} dollars"
print(txt)
tax=0.25
txt=f"The price is {price+(price*tax)} dollars"
print(txt)
txt=f"It is very {"Expensive" if price>50 else "Cheap"}"
print(txt)
print(f"\nFunctions in F-Strings\n")
fruit="apples"
txt=f"I love {fruit.upper()}"
print(txt)
def myConverter(x):
    return x*0.3048
txt=f"The plane is flying at a {myConverter(30000)} meter altitude"
print(txt)