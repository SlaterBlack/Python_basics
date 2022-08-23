filename=input("File name: ")
try:
    infile = open(filename)
except:
    print("that file does not exist")
wordcount=0

linecount= len(infile.readlines())
infile.close()
charactercount=0
infile = open(filename)
data=infile.read()
infile.close()
words=data.split()
wordcount=len(words)
charactercount=len(data)
print(f'Characters: {charactercount}')
print(f'Words: {wordcount}')
print(f'Lines: {linecount}')