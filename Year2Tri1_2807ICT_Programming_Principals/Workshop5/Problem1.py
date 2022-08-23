stop=0
store=0
count=0
while (stop==0):
    s = str(input('please enter a sentence: '))
    n=0
    for c in s:
        if n==0 and (c=='a' or c=='A'):
            stop=1
        n=n+1
    if n>store:
        endline=s
        store=n
        n=0
print(f'Longest was: {endline}')