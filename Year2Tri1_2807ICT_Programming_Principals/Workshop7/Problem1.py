try:
    infile = open(input("Source file name: "))
except:
    print("that file does not exist")
    count=0
content=infile.read()
contentlst=content.split(' ')
for i in range(len(contentlst)):
    if contentlst[i]=='file':
        count+=1
infile.close()
print(f'number of times the the word file appeared: {count}')