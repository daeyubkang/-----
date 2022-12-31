import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
list1 = list(map(int, input().split()))
list1.sort()
i =0
j =n-1
count = 0

while(i<j):
    if list1[i] + list1[j] < m:
        i +=1
    elif list1[i] + list1[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)

