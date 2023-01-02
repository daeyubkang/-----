from collections import deque
import sys
input = sys.stdin.readline

a = deque()
n = int(input())

for i in range(1,n+1):
    a.appendleft(i)

while len(a) > 1:
    a.pop()
    b = a.pop()
    a.appendleft(b)

print(a.pop())
