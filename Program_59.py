# Lambda Function in Python

x=lambda a:a+10
print(x(5))
x=lambda a,b:a*b
print(x(5,6))
x=lambda a,b,c:a+b+c
print(x(5,6,2))
def myfunc(n):
    return lambda a:a*n
myDoubler=myfunc(2)
print(myDoubler(11))
myTripler=myfunc(3)
print(myTripler(11))