import sys
input = sys.stdin.readline

n = int(input())
a = [0]*n

for i in range(n):
    a[i] = (int(input()))

stack = []
num =1
answer = []

for i in range(n):
    if(a[i] >= num):
        while(num <= a[i]):
            stack.append(num)
            num += 1
            answer.append("+")
        stack.pop()
        answer.append("-")
    else:
        q = stack.pop()
        if q > a[i]:
            print("NO")
            result =False
            break
        else:
            answer.append("-")

print(answer)