import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

a.sort()
max = a[0]
full = []
full.append(max)
qwe =0 

for i in range(1,n):
    max = a[i] + max
    full.append(max)

for i in range(n):
    qwe = qwe + full[i]
print(qwe)