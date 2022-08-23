def year_diff(x,y):
    check=x
    count=0
    for z in range(x,(y+1)):
        if z%4==0:
            count=count+366
        else:
            count=count + 365
        check+=1
    print(count)

year1=int(input('Year 1? '))
year2=int(input('Year 2? '))
year_diff(year1,year2)
