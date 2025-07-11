# Arrays in Python

cars=["Ford","Volvo","BMW"]
print(cars)
print(cars[0])
cars[0]="Toyota"
print(cars)
print(len(cars))
for x in cars:
    print(x)
cars.append("Honda")
print(cars)
cars.remove("Volvo")
print(cars)
cars.pop(1)
print(cars)