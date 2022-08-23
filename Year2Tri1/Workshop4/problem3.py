number=int(input('please enter a positive number'))
for i in range(1, (2*number)+1):
  i = i - (number+1)
  if i < 0:
    i = -i
  print(" " * i + "*" * ((number+2) - i*2) + " "*i)
