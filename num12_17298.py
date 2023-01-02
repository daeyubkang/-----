import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int,input().split()))

stack = []
a= [0]*n

for i in range(n):
    while stack and number[stack[-1]]<number[i]:
        a[stack.pop()] = number[i]
    stack.append(i)

while stack:
    a[stack.pop()] = -1

print(a)