# Copy Dictionaries in Python

myDict={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}
copiedDict=myDict.copy()
print(copiedDict)
copiedDict=dict(myDict)
print(copiedDict)