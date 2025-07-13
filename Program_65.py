# Scope in Python

print(f"\nLocal Scope\n")
def myFunc():
    x=100
    print(x)
myFunc()
def myFunc():
    x=200
    def myInnerFunc():
        print(x)
    myInnerFunc()
myFunc()
print(f"\nGlobal Scope\n")
x=300
def myFunc():
    print(x)
myFunc()
print(x)
print(f"\nNaming Variables\n")
x=400
def myFunc():
    x=500
    print(x)
myFunc()
print(x)
print(f"\nGlobal Keyword\n")
def myFunc():
    global x
    x=600
myFunc()
print(x)
x=700
def myFunc():
    global x
    x=800
myFunc()
print(x)
print(f"\nNonlocal Keyword\n")
def myFunc1():
    x="Jane"
    def myFunc2():
        nonlocal x
        x="hello"
    myFunc2()
    return x
print(myFunc1())