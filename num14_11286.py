from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
b = deque()
qwe = []

for i in range(n):
    a = int(input())
    if(a == 0):
        if(b):
            qwe.append(b.popleft())
        else:
            qwe.append(0)
    else:
        if(b):
            q = b[-1]
            w = b[0]
            if (abs(a) > abs(q)):
                b.append(a)
            elif (abs(a) == abs(q)):
                if a >= q:
                    b.append(a)
                else:
                    count=0
                    while(a<q):
                        b.rotate(1)
                        q = b[-1]
                        count += 1
                        if (count==len(b)):
                            break
                    if (count==len(b)):
                        b.appendleft(a)
                    else:
                        b.append(a)
                        b.rotate(-count)
            else:
                count = 0
                while(abs(a)<abs(q)):
                    b.rotate(1)
                    q = b[-1]
                    count += 1
                if(abs(a)==abs(q)):
                    if a >= q:
                        b.append(a)
                    else:
                        count=0
                        while(a<q):
                            b.rotate(1)
                            q = b[-1]
                            count += 1
                        b.append(a)
                        b.rotate(-count)
                else:
                    b.append(a)
                    b.rotate(-count)   
        else:
            b.appendleft(a)

print(qwe)


