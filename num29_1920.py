import sys
input = sys.stdin.readline

n = int(input())
mylist = list(map(int,input().split()))
find = int(input())
findlist = list(map(int,input().split()))

mylist.sort()

for i in findlist:
    start =0
    end = (len(mylist) - 1)
    correct =False
    while(start<=end):
        middle = (end+start)//2
        if i < mylist[middle]:
            end = middle -1
        elif i > mylist[middle]:
            start = middle +1
        else:
            correct = True
            break
    if correct:
        print(1)
    else:
        print(0)
