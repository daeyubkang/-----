import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

testcase = int(input())

def findcycle(v):
    global result
    b[v] = True
    for i in a[v]:
        if b[i] == False:
            color[i] = (color[v]+1)%2
            findcycle(i)
        elif color[v] == color[i]:
                result = False

final_result = []

for i in range(testcase):
    n,e = map(int,input().split())
    a = [[]for _ in range(n+1)]
    b = [False] * (n+1)
    for j in range(e):
        q,w = map(int,input().split())
        a[q].append(w)
        a[w].append(q)

    for i in range(1,n+1):
        color = [0] * (n+1)
        color[i] = 1
        result = True
        findcycle(i)
        if result == False:
            break
    final_result.append(result)

for i in final_result:
    if i == False:
        print("NO")
    else:
        print("YES")
    
    
