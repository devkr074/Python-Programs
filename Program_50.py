# Looping through Dictionaries in Python

myDict={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964,
  "color":"Red"
}
for x in myDict:
   print(x)
for x in myDict:
   print(myDict[x])
for x in myDict.values():
   print(x)
for x in myDict.keys():
   print(x)
for x,y in myDict.items():
   print(x,y)