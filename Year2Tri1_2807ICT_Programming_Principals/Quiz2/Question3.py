nums=[1,1,2,1]
ongoing=0
out=0
for h in range(len(nums)-2):
    if ((nums[h+2]-nums[h+1])==(nums[h+1]-nums[h])):
        ongoin=1
    if (ongoing==0 and ((nums[h+2]-nums[h+1])==(nums[h+1]-nums[h]))):
        out+=1
        ongoing=1
    if (ongoing==1 and ((nums[h+2]-nums[h+1])==(nums[h+1]-nums[h]))):
        ongoing=0
print(f'output: {out}')
