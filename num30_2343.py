import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))

sum1 = sum(a)
max1 = max(a)

start = max1
end = sum1
qwe =[]
result = []

while(start<=end):
    middle = (start + end) // 2
    sum2 = 0
    qwe.clear()
    for i in range(n):
        if sum2 + a[i] > middle:
            qwe.append(sum2)
            sum2 = 0
        sum2 += a[i]
    if sum2 > 0:
        qwe.append(sum2)
    if len(qwe)>m:
        start = middle + 1
    elif len(qwe)<m:
        end = middle - 1
    else:
        result.append(middle)
        end = middle -1

if(len(result)==0):
    print(middle)
else:
    print(min(result))
        