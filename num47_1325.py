import sys
input = sys.stdin.readline
from collections import deque

n,e = map(int,input().split())

a = [[]for i in range(n+1)]
count1 = [0] * (n+1)

for i in range(e):
    q,w = map(int,input().split())
    a[q].append(w)

def findnum(v):
    queue = deque()
    queue.append(v)
    b[v] = True
    while queue:
        now_node = queue.popleft()
        for i in a[now_node]:
            if b[i] == False:
                b[i] = True
                count1[i] += 1
                queue.append(i)

max1 = 0
for i in range(1,n+1):
    b = [False] * (n+1)
    findnum(i)

for i in range(1,n+1):
    if max1 < count1[i]:
        max1 = count1[i]

for i in range(1,n+1):
    if max1 == count1[i]:
        print(i,end=" ")



