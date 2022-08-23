
def checkarithmatic(check):
    count=0
    change=(check[1]-check[0])
    for k in range(len(check)-1):
        if not ((int(check[i+1])-int(check[i]))==change):
            count+=1
    if count>0:
        print(f'{check} True')
    else:
        print(f'{check} False')


filename=input("File name: ")
number=[]
try:
    infile = open(filename,mode='r')
except:
    print("that file does not exist")    
for i in infile:
    nums=infile.readline()
    nums=nums.split(' ')
    for k in range(len(nums)):
        number.append(int(nums[k]))
    for i in range (len(nums)):
        checkarithmatic(number)
    
infile.close()