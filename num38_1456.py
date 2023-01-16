import math,sys
input = sys.stdin.readline

n,m = map(int,input().split())

m1 = int(math.sqrt(m))
n1 = int(math.sqrt(n))

a = [0]*(m1+1)
count = 0

for i in range(m1+1):
    a[i] = i

for i in range(2,int(math.sqrt(m1)+1)):
    if a[i] == 0:
        continue
    for j in range(i,m1//i+1):
        a[i*j] = 0

for i in range(2,m1+1):
    if a[i] > 1:
        l = 2
        while (i**l) <= m:
            if i**l >= n:
                count +=1
            l += 1

print(count) 
