import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,e = map(int,input().split())
a = [[]for i in range(n)]
b = [0] * n
z = 0

for i in range(e):
    q,w = map(int,input().split())
    a[q].append(w)
    a[w].append(q)

def count(v,depth):
    global z
    if depth ==5:
        z =1
        return
    b[v] = 1
    for i in a[v]:
        if b[i]==0:
            count(i,depth+1)
    b[v] = 0


for i in range(n):
    b = [0]* n
    s = 0
    if a[i]:
        count(i,1)
        if z==1:
            break

print(z)