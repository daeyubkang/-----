import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = []


for i in range(n):
    q = int(input())
    a.append(q)

result = 0

for i in reversed(range(n)):
    if (m>=a[i]):
        result += m//a[i]
        m = m - (m//a[i])*a[i]
    if(m==0):
        break

print(result)