import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, e = map(int,input().split())
a = [[]for i in range(n+1)]
b = [0] * (n+1)
count = 0


def dfs(v):
    b[v] = 1
    for i in a[v]:
        if b[i] == 0:
            dfs(i)

for i in range(e):
    q,w = map(int,input().split())
    a[q].append(w)
    a[w].append(q)

for i in range(1,n+1):
    if b[i] == 0:
        count += 1
        dfs(i)

print(count)

        


    