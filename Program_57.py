# Functions in Python

print(f"\nUsing Function\n")
def my_function():
    print("Hello from a function")
my_function()
print(f"\nUsing Function with Parameters\n")
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
print(f"\nUsing Function with Multiple Unknown Parameters\n")
def my_function(*kids):
    print("The youngest child is "+kids[2])
my_function("Emil","Tobias","Linus")
print(f"\nUsing Function with Keyword Arguments\n")
def my_function(child3,child2,child1):
    print("The youngest child is "+child3)
my_function(child1="Emil",child2="Tobias",child3="Linus")
print(f"\nUsing Function with Keyword Arguments with Multiple Unknown Parameters\n")
def my_function(**kid):
    print("His last name is "+kid["lname"])
my_function(fname="Tobias",lname="Refsnes")
print(f"\nUsing Function with Default Parameter Value\n")
def my_function(country="Norway"):
    print("I am from "+country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print(f"\nUsing Function with List as Parameter\n")
def my_function(food):
    for x in food:
        print(x)
fruits=["Apple","Banana","Cherry"]
my_function(fruits)
print(f"\nUsing Function with Return Value\n")
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))
print(f"\nUsing pass Statement in Function\n")
def myfunction():
    pass
print(f"\nUsing Positional-Only Arguments Function\n")
def my_function(x,/):
    print(x)
my_function(3)
print(f"\nUsing Keyword-Only Arguments Function\n")
def my_function(*,x):
    print(x)
my_function(x=3)
print(f"\nUsing Combination of Positional-Only and Keyword-Only Arguments Function\n")
def my_function(a,b,/,*,c,d):
    print(a+b+c+d)
my_function(5,6,c=7,d=8)