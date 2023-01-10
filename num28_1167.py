import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000)

n = int(input())
a = [[]for i in range(n+1)]
v = [0] * (n+1)
start = 0

for i in range(1,n+1):
    b = list(map(int,input().split()))
    w = 1
    s = b[0]
    while(w < (len(b)-2)):
        a[s].append((b[w],b[w+1]))
        w +=2

def check(q):
    for i,j in a[q]:
        if v[i] == 0 and i != start:
            v[i] = v[q] + j
            check(i)

start = 1
check(1)
index1 = v.index(max(v))
v = [0] * (n+1)
start = index1
check(index1)
print(max(v))
