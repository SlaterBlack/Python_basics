from posixpath import split


inp = list(map(int,input("please enter two integer values").split()))
if (inp[0]>0 and inp[0]<100 and inp[0]<inp[1]) or (inp[0]>=(2*inp[1]) and (inp[1]<-8 or inp[1]>16 or inp[1]==0)):
    print('True')
else:
    print('False')