import sys
input = sys.stdin.readline
from collections import deque

def isprime(num):
    for  i in range(2,int(num/2+1)):
        if num % i ==0:
            return False
    return True

n = int(input())
a = deque()
a.append(2)
a.append(3)
a.append(5)
a.append(7)
b = [1,3,5,7,9]
q = 1

while(q<n):
    len1 = len(a)
    for i in range(len1):
        for j in range(5):
            w = (a[i]*10) + b[j]
            if isprime(w):
                a.append(w)
    for i in range(len1):
        a.popleft()
    q += 1

for i in a:
    print(i)

