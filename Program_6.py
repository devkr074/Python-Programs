# Local and Global Variables in Python

def func():
    x=5
    print(x)
func()
# print(x)    # Error as x is a local variable

y=10
def func1():
    print(y)
func1()
print(y)

def func2():
    global z
    z=15
    print(z)
func2()
print(z)