import sys
print = sys.stdout.write

a = list(input())

a.sort(reverse=True)

for i in range(len(a)):
    print(a[i])