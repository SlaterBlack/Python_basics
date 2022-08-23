test=list(str(input('String: ')))
happy=0
count=0
hold=0
for c in test:
    if (c=='g') and hold==1:
        happy=1
    count+=1
    if c=='g':
        hold=1
if happy==1:
    print('Happy? True')
else:
    print('Happy? False')
