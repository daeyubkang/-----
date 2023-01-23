import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

a = [0]*(n+1)
print_result = []

for i in range(n+1):
    a[i] = i

def find_num(v):
    if a[v] != v:
        a[v] = find_num(a[v])
    return a[v]

for i in range(m):
    q,w,e = map(int,input().split())
    result = 0
    if q == 0:
        e1 = find_num(e)
        w1 = find_num(w)
        if e1 > w1:
            a[e1] = a[w1]
            a[e] = a[w1]
        else:
            a[w1] = a[e1]
            a[w] = a[e1]
    else:
        q1 = find_num(w)
        q2 = find_num(e)
        if q1 == q2:
            print_result.append("YES")
        else:
            print_result.append("NO")

for i in print_result:
    print(i)

print(a)