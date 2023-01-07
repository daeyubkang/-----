import sys
from collections import deque
input = sys.stdin.readline

n,e,start = map(int,(input().split()))
a =[[]for i in range(n+1)]
ab = [False] * (n+1)

for i in range(e):
    q,w = map(int,input().split())
    a[q].append(w)
    a[w].append(q)

for i in range(n):
    a[i].sort()

def dfs(st):
    print(st, end=' ')
    ab[st] = True
    for i in a[st]:
        if not ab[i]:
            dfs(i)

def bfs(st):
    queue = deque()
    queue.append(st)
    ab[st] = True
    while queue:
        now_node = queue.popleft()
        print(print(now_node), end = ' ')
        for i in a[now_node]:
            if not ab[i]:
                ab[i] =True
                queue.append(i)

dfs(start)

ab = [False] * (n+1)
bfs(start)

        
