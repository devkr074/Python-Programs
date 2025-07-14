# Modules in Python

import MyModule as mx
from MyModule import person1 as p1
import platform
mx.greeting("Jonathan")
a=mx.person1["age"]
print(a)
print(p1)
x=platform.system()
print(x)
x=dir(platform)
print(x)