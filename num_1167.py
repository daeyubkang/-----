import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

n = int(input())
a = [[0 for j in range(n+1)]for i in range(n+1)]
f = [[]for i in range(n+1)]
v = [0] * (n+1)
max1 = 0
max2 = []
myque = []

for i in range(1,n+1):
    b = list(map(int,input().split()))
    w = 1
    while(w < (len(b)-2)):
        a[i][b[w]] = b[w+1]
        f[i].append(b[w])
        w +=2

def check(myque):
    global max1
    qwe = []
    for i in range(len(myque)-1):
        be = myque[i]
        af = myque[i+1]
        if be==myque[0]:
            qwe.append(max1)
            max1 = 0
        max1 = max1 + a[be][af]
    qwe.append(max1)
    max2.append(max(qwe))


def makePath(m):
    global count
    v[m] = 1
    myque.append(m)
    for i in f[m]:
        if v[i] == 0:
            if count[m]>0:
                check(myque)
                myque.pop()
            count[m] += 1
            makePath(i) 

for i in range(1,n+1):
    v = [0] * (n+1)
    max1 = 0
    count = [0] * (n+1)
    myque.clear()
    if(f[i]):
        makePath(i)
        check(myque)

print(max(max2))