import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append((int(input()),i))

sorta = sorted(a)
max = 0

for i in range(n):
    if max < sorta[i][1]-i:
        max = sorta[i][1] - i

print(max+1)
