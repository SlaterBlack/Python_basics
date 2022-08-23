from curses.ascii import isdigit
try:
    infile = open(input("Source file name: "))
except:
    print("that file does not exist")
outfile = open(input("Target file name: "), mode = 'w')
counter = 0
for i in infile:
    if isdigit(infile.readline(1)):
        continue
    outfile.write(i)
infile.close()
outfile.close()