# Access Dictionary Items in Python

myDict={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
x=myDict["model"]
print(x)
x=myDict.get("brand")
print(x)
x=myDict.keys()
print(x)
myDict["color"]="White"
print(x)
x=myDict.values()
print(x)
myDict["year"]=2020
print(x)
x=myDict.items()
print(x)