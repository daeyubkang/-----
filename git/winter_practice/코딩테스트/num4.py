import sys
input = sys.stdin.readline

n, quizNo = map(int, input().split())
a = [[0 for j in range(n+1)] for i in range(n+1)]
sum = [[0 for j in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    q = 1
    for j in map(int,input().split()):
        a[i][q] = j
        q = q+1

sum[1][1] = a[1][1]
for i in range(2, n+1):
    sum[i][1] = sum[i-1][1] + a[i][1]
    sum[1][i] = sum[1][i-1] + a[1][i]

for i in range(2, n+1):
    for j in range(2, n+1):
        sum[i][j] = a[i][j] + sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1]

print(a)
print(sum)

for i in range(quizNo):
    x1,y1,x2,y2 = map(int,input().split())
    print(sum[x2][y2] + sum[x1-1][y1-1] - sum[x2][y1-1] - sum[x1-1][y2])
