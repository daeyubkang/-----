import sys,math

a, b = map(int,input().split())
qw = [0] * (b-a+1)
count =0
for i in range(2,int(math.sqrt(b))+1):
    asd = i*i
    start = a%asd
    if start != 0:
        for j in range(a//asd+1,b//asd+1):
            count =asd*j-a
            qw[count] = 1
            
    else:
        for j in range(a//asd,b//asd+1):
            count = asd*j-a
            qw[count] = 1
            
result = 0
for i in range(len(qw)):
    if qw[i] == 0:
        result += 1

print(result)



