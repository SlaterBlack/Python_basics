y=0
x=0
grade=[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0],[0,0,0,0]
average=[0,0,0,0,0]
count=0
for  h in range(5): 
    print(f'student {count+1}')
    grade[count][0]=int(input(''))
    grade[count][1]=int(input(''))
    grade[count][2]=int(input(''))
    grade[count][3]=int(input(''))
    count+=1
count=0
for p in range(5):
    temp1=int(sum(grade[count]))
    average[count]=temp1/4
    count+=1
print(f'The highest average mark of students:{max(average[0],average[1],average[2],average[3])}')
print(f'The highest average course of students:{max([float(sum(n))/len(n) for n in zip(*grade)])}')