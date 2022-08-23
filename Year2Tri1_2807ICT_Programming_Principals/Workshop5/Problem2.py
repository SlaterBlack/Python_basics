s = list(str(input('Input a string? ')))
count=0
for c in s:
    if c.isnumeric():
        s[count]='_'
    count+=1
print(f'Output: {"".join(s)}')
