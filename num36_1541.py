import sys
input = sys.stdin.readline

a = list(map(str,input().split("-")))

def mysum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

result = 0
count = 0 

for i in a:
    temp = mysum(i)
    if count == 0:
        result = temp
        count += 1
        continue
    result -= temp

print(result)