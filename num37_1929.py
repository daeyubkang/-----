import sys
input = sys.stdin.readline
import math

n,m = map(int,input().split())

a = [0] *(m+1)

for i in range(m+1):
    a[i] = i

for i in range(2,int(math.sqrt(m))+1):
    if a[i] == 0:
        continue
    for j in range(i,m//i+1):
        a[i*j] = 0

for i in range(n,m+1):
    if a[i]>1:
        print(i)

