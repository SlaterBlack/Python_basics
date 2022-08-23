#Workshop3 Problem 2
base = float(input('How much is the base price? '))
weight = float(input('What is the weight? '))
distance = float(input('What is the distance? '))
discount = 1.0
if distance >= 250:
    discount = 0.1
if distance >= 500:
    discount = 0.15
if distance >= 1000:
    discount = 0.2
if distance >= 2000:
    discount = 0.35
if distance >= 3000:
    discount = 0.5
shipping = base * weight * distance * (1 - discount)
print(shipping)