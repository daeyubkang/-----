import sys

n = int(input())

a=[]

for i in range(n):
    q,w = map(int,input().split())
    a.append((q,w))

for i in range(len(a)):
    q,w = a[i]
    if w>q:
        q,w=w,q
    x = 1
    while(x!=0):
        x = q%w
        q,w = w,x
    d,f = a[i]
    result = q*(d//q)*(f//q)
    print(result)