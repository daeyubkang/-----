import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())
qw = PriorityQueue()
qwe = PriorityQueue()
result = 0

for i in range(n):
    q = int(input())
    if q>0:
        qw.put(-q)
    else:
        qwe.put(q)

while(qw.qsize()>0):
    if qw.qsize() >1:
        a = qw.get()
        b = qw.get()
        if a==-1 or b==-1:
            result += -(a+b)
            continue
        result += a*b
    elif qw.qsize() == 1:
        a = qw.get()
        result += -a

while(qwe.qsize()>0):
    if qwe.qsize() >1:
        a = qwe.get()
        b = qwe.get()
        result += a*b
    elif qwe.qsize() == 1:
        a = qwe.get()
        result += a

print(result)

