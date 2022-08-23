inp=66
out=[0,0,0,0,0]
while inp>=50:
    out[0]+=1
    inp-=50
while inp>=20:
    out[1]+=1
    inp-=20
while inp>=10:
    out[2]+=1
    inp-=10
while inp>=5:
    out[3]+=1
    inp-=5
while inp>=1:
    out[4]+=1
    inp-=1

print(out)
