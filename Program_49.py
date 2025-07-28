# Remove Dictionary Items in Python

myDict={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964,
  "color":"Red"
}
myDict.pop("model")
print(myDict)
myDict.popitem()
print(myDict)
del myDict["brand"]
print(myDict)
myDict.clear()
print(myDict)
del myDict
print(myDict)