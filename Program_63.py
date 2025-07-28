# Iterators in Python

print(f"\nIterators in Python\n")
myTuple=("Apple","Banana","Cherry")
myIt=iter(myTuple)
print(next(myIt))
print(next(myIt))
print(next(myIt))
myStr="Banana"
myIt=iter(myStr)
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(f"\nLooping through an Iterator\n")
myTuple=("Apple","Banana","Cherry")
for x in myTuple:
    print(x)
myStr="Banana"
for x in myStr:
    print(x)
print(f"\nCreating an Iterator\n")
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myClass=MyNumbers()
myIter=iter(myClass)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(f"\nStopIteration\n")
class MyNumbers:
    def __iter__(self):
       self.a=1
       return self
    def __next__(self):
       if self.a<=20:
          x=self.a
          self.a+=1
          return x
       else:
          raise StopIteration
myClass=MyNumbers()
myIter=iter(myClass)
for x in myIter:
    print(x)