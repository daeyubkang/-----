import sys
input = sys.stdin.readline

n= int(input())
m = list(map(int,input().split()))
count = 0 

m.sort()

for k in range(n):
    i = 0
    j = n-1
    while(i<j):
        if(m[k] == m[i]+m[j]):
            if(k != i and k != j):
                count +=1
                break
            elif(k == i):
                i += 1
            else:
                j -= 1
        elif(m[k] < m[i]+m[j]):
            j -= 1
        else:
            i += 1

print(count)
