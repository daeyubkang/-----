import sys
input = sys.stdin.readline

n = int(input())
a = [[0]*2 for i in range(n)]

def findnum(a,b):
    result = 1
    while(result != 0):
        result = a%b
        a,b = b,result
    return a

for i in range(n-1):
    q,w,e,r = map(int,input().split())
    if r>e:
        q,w,e,r = w,q,r,e
    number = findnum(e,r)
    qnum = e//number
    wnum = r//number
    if a[q][0] == 0 and a[w][0] == 0:
        a[q][0] = qnum
        a[w][0] = wnum
        a[q][1] = w
        a[w][1] = q
    elif a[q][0] != 0 and a[w][0] == 0:
        if a[q][0] >= qnum:
            if a[q][0]%qnum == 0:
                a[w][0] = a[q][0]//qnum*wnum
                a[q][1] = w
                a[w][1] = q
            else:
                a[w][0] = a[q][0]*wnum
                a[q][1] = w
                a[w][1] = q
                for i in range(n):
                    if i == w:
                        continue
                    if a[i][0] != 0:
                        a[i][0] = a[i][0]*qnum
        else:
            if qnum%a[q][0] ==0:
                for i in range(n):
                    if i ==q or i == w:
                        continue
                    a[i][0] = a[i][0]*(qnum//a[q][0])
                a[q][0] = qnum
                a[w][0] = wnum
                a[q][1] = w
                a[w][1] = q
            else:
                for i in range(n):
                    if a[i][0] != 0:
                        if i == q or i == w:
                            continue
                        a[i][0] = a[i][0]*qnum
                a[w][0] = wnum*a[q][0]
                a[q][0] = a[q][0]*qnum
                a[q][1] = w
                a[w][1] = q 
    elif a[q][0] ==0 and a[w][0] != 0:
        if a[w][0] >= wnum:
            if a[w][0]%wnum == 0:
                a[q][0] = a[w][0]//wnum*qnum
                a[q][1] = w
                a[w][1] = q
            else:
                a[q][0] = a[w][0]*qnum
                a[q][1] = w
                a[w][1] = q
                for i in range(n):
                    if i == q:
                        continue
                    if a[i][0] != 0:
                        a[i][0] = a[i][0]*wnum
        else:
            if wnum%a[w][0] ==0:
                for i in range(n):
                    if i == w or i == q:
                        continue
                    a[i][0] = a[i][0]*(wnum//a[w])
                a[q][0] = qnum
                a[w][0] = wnum
                a[q][1] = w
                a[w][1] = q
            else:
                for i in range(n):
                    if a[i][0] != 0:
                        if i == q or i == w:
                            continue
                        a[i][0] = a[i][0]*wnum
                a[q][0] = qnum*a[w][0]
                a[w][0] = a[w][0]*wnum
                a[q][1] = w
                a[w][1] = q
    else:
        seed = a[q][0]*a[w][0]
        for i in range(n):
            if i == q or i == w:
                continue
            if a[i][1] == q:
                a[i][0] = ((seed*qnum)//a[q][0])*a[i][0]
                continue
            if a[i][1] == w:
                a[i][0] = ((seed*wnum)//a[w][0])*a[i][0]
                continue
            a[i][0] = a[i][0] * seed
        a[q][0] = seed * qnum
        a[w][0] = seed * wnum

for i in range(n):
    if i == (n-1):
        print(a[i][0])
        break
    print(a[i][0],end=" ")
