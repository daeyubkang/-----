checkList = [0] * 4
myList = [0] * 4
checkSecret = 0

def myadd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] +=1
        if myList[0] ==checkList[0]:
            checkSecret +=1
    elif c == 'C':
        myList[1] +=1
        if myList[1] ==checkList[1]:
            checkSecret +=1
    elif c == 'G':
        myList[2] +=1
        if myList[2] ==checkList[2]:
            checkSecret +=1
    elif c == 'T':
        myList[3] +=1
        if myList[3] ==checkList[3]:
            checkSecret +=1

def remove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] ==checkList[0]:
            checkSecret -=1
    elif c == 'C':
        if myList[1] ==checkList[1]:
            checkSecret -=1
    elif c == 'G':
        if myList[2] ==checkList[2]:
            checkSecret -=1
    elif c == 'T':
        if myList[3] ==checkList[3]:
            checkSecret -=1

s,p = map(int,input().split())
result = 0
a = list(input())
checkList = list(map(int,input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(p):
    myadd(a[i])

if checkSecret == 4:
    result += 1

for i in range(p,s):
    j = i - p
    myadd(a[i])
    remove(a[j])
    if checkSecret == 4:
        result += 1

print(result)