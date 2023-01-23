import sys

a,b,c = map(int,input().split())

def findnum(a,b):
    if b == 0:
        return 1,0
    correct = a//b
    result = a%b
    e,r = findnum(b,result)
    resultx = r
    resulty = e-r*correct
    return resultx,resulty
    

ax,bx,cx = a,b,c
while(bx != 0):
    resultx = ax%bx
    ax,bx = bx,resultx

if cx%ax !=0:
    print(-1)
else:
    x,y=findnum(a,b)
    x *= c//ax
    y *= c//ax
    print(x,y)

