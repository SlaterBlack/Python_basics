long = float(input("How long is the park?"))
wide = float(input("How wide is the park?"))
fill = float(input("how many litres needed per square metre"))
total = float((long * wide)*fill)
print(f'litres required: {total}')