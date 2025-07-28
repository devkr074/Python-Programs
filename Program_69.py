# JSON in Python

import json
print(f"\nJSON to Python\n")
x='{"name":"John","age":30,"city":"New York"}'
y=json.loads(x)
print(y)
print(f"\nPython to JSON\n")
x={
    "name":"John",
    "age":30,
    "city":"New York"
}
y=json.dumps(x)
print(y)
x={
    "name":"John",
    "age":30,
    "married":True,
    "divorced":False,
    "children":("Ann","Billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"Ford Edge","mpg":24.1}
    ]
}
print(json.dumps(x))
print(json.dumps(x,indent=4))
print(json.dumps(x,indent=4,separators=(".","=")))
print(json.dumps(x,indent=4,sort_keys=True))