from unicodedata import numeric
(list1)=[0]
list2=[0]
count=0
print('list1: ')
countcheck1=0
countcheck2=0
listcheck=0
while (listcheck==0):
    hold=(input(''))
    if hold.isnumeric():
        list1.append(hold)
        countcheck1+=1
    else:
        listcheck=1
listcheck=0
print('list2: ')
while (listcheck==0):
    hold=int(input(''))
    if hold.isnumeric():
        list2.append(hold)
        countcheck2+=1
    else:
        listcheck=1

if countcheck1 == 1:
    sum1=list1[1]
if countcheck1 > 1:
    sum1=int(list1[-1]) - int(list1[1])
if countcheck2 == 1:
    sum2=(list2[1])
if countcheck2 > 1:
    sum2=int(list2[-1]) - int(list2[1])
if  sum1==sum2:
    print('Output: same')
else:
    final=max(sum1,sum2)
    print(f'Output: {final}')
    