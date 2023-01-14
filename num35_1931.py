# import sys
# input = sys.stdin.readline
# from queue import PriorityQueue

# n = int(input())
# a = PriorityQueue()
# qw = [[0,0]]
# print(len(qw))

# for i in range(n):  
#     q,w = map(int,input().split())
#     a.put((q,w))

# for i in range(n):
#     s,d = a.get()
#     count = 0
#     for i in range(len(qw)):
#         if qw[i][0] <= s:
#             qw[i][0] = d
#             qw[i][1] += 1
#             count += 1
#     if count == 0:
#         qw.append([d,1])

# max = 0
# for i,j in qw:
#     if max < j:
#         max = j

# print(max)

import sys
input = sys.stdin.readline

n = int(input())
qw = [[0]*2 for i in range(n)]

for i in range(n):  
    q,w = map(int,input().split())
    qw[i][0] = w
    qw[i][1] = q

qw.sort()
end = -1
count = 0

for i in range(n):
    if end <= qw[i][1]:
        end = qw[i][0]
        count += 1

print(count)


        