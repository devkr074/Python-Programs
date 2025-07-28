# Try Except in Python

print(f"\nException Handling\n")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occured")
print(f"\nelse Keyword\n")
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
print(f"\nFinally Block\n")
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
try:
    f=open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
print(f"\nRaise an exception\n")
x=-1
if x<0:
    raise Exception("Sorry, no numbers below zero")
x="Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")