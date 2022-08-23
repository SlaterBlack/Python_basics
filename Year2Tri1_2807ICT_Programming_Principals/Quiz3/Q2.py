try:
    infile = open(input("Source file name: "))
except:
    print("that file does not exist")
content=infile.read()

infile.close()
print(content)