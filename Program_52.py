# Nested Dictionaries in Python

familyDict={
  "child1":{
    "name":"Emil",
    "year":2004
  },
  "child2":{
    "name":"Tobias",
    "year":2007
  },
  "child3":{
    "name":"Linus",
    "year":2011
  }
}
print(familyDict)
child1={
  "name":"Emil",
  "year":2004
}
child2={
  "name":"Tobias",
  "year":2007
}
child3={
  "name":"Linus",
  "year":2011
}
familyDict={
  "child1":child1,
  "child2":child2,
  "child3":child3
}
print(familyDict)
print(familyDict["child2"]["name"])
for x,obj in familyDict.items():
    print(x)
    for y in obj:
        print(y,":",obj[y])