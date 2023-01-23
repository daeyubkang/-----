import sys
input = sys.stdin.readline

n,m = map(int,input().split())
result = 1
if m>n:
    n,m=m,n
while(result!=0):
    result = n%m
    n,m = m,result

for i in range(n):
    print(1,end="")
