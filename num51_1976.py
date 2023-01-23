import sys
input = sys.stdin.readline

n = int(input())
route = int(input())

a = [[0 for i in range(n+1)]for _ in range(n+1)]
union_list = [0] * (n+1)

for i in range(n+1):
    union_list[i] = i

def find(v):
    if union_list[v] != v:
        union_list[v] = find(union_list[v])
    return union_list[v]

def union(a,b):
    z = find(a)
    x = find(b)
    if z > x:
        union_list[z] = x
        find(a)
    else:
        union_list[x] = z
        find(b)

for i in range(1,n+1):
    qwe = list(map(int,input().split()))
    for j in range(n):
        if qwe[j] == 1:
            a[i][j+1] = 1
            union(i,j+1)

for i in union_list:
    qwer = find(i)

plan = list(map(int,input().split()))
printsign = False

for i in range(1,len(plan)):
    plan1 = plan[i-1]
    plan2 = plan[i]
    if union_list[plan1] != union_list[plan2]:
        printsign = True
        break

if printsign == True:
    print("NO")
else:
    print("YES")