num=int(input("Number of rows"))
len_n=num+1
count=1
for c in range(num):
    print(count*'+' + (len_n-count)*"o")
    count+=1