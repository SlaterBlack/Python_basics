stop=0
count=0
while (stop==0):
    s = str(input('Enter a string: '))
    count+=1
    if s[-1]=='.':
        stop=1
print(f'{count} strings were entered.')