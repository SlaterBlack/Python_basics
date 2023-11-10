#   Converts given time in hours, minutes and seconds into seconds
def time_to_seconds (hour, minute,seconds): 
    out=((hour*3600)+(minute*60)+(seconds))
    return out

#factorial code
n=int(input('Input: '))
count=0
while n>0:
    count+=n
    n-=1
print(f'Output: {count}')