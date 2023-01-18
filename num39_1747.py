import math
from collections import deque

n = int(input())

a = [0] * 1000001

for i in range(1,1000001):
    a[i] = i

for i in range(2, int(math.sqrt(1000000))+1):
    if a[i] == 0:
        continue
    for j in range(i,1000000//i+1):
        a[i*j] = 0

count = True

for i in range(n,1000001):
    if a[i]>1:
        st = str(a[i])
        qwe = deque(st)
        while len(qwe) > 1:
            count = True
            front = qwe.popleft()
            rear = qwe.pop()
            if front != rear:
                count = False
                break
        if count == True:
            print(i)
            break
    if(i == 1000000):
        print(1003001)



