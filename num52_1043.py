import sys
input = sys.stdin.readline

n,p = map(int,input().split())
know_true = list(map(int,input().split()))

a = [0] * (n+1)
remember = [[]for i in range(p)]

for i in range(n+1):
    a[i] = i

def find(v):
    if a[v] != v:
        a[v] = find(a[v])
    return a[v]

for i in range(p):
    party = list(map(int,input().split()))
    remember[i] = party
    if party[0]>1:
        for j in range(1,party[0]):
            q = find(party[j])
            w = find(party[j+1])
            if q > w:
                a[q] = w
                find(party[j])
            else:
                a[w] = q
                find(party[j+1])

for i in range(n+1):
    find(i)

for i in range(1,know_true[0]+1):
    q = find(know_true[i])
    a[q] = 0

count = 0

for i in range(p):
    result1 = False
    number1 = int(remember[i][0])
    for j in range(1,number1+1):
        qwe = remember[i][j]
        qwer = a[a[qwe]]
        if qwer == 0:
            result1 += True
            break
    if result1 == False:
        count += 1

print(count)
            

        



