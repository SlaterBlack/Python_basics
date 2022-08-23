filename=input("File name: ")
try:
    infile = open(filename)
except:
    print("that file does not exist")
count=0
counter = 0 
print("Output:")
for i in infile:
    counter+=1
infile.close()
infile = open(filename)
for i in infile:
    if count==0:
        print (i)
    if count==1: 
        print (i)
    if count==(counter-2):
        print (i)
    if count==(counter-1):
        print (i)
    count+=1 
infile.close()
