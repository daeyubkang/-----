import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())
pq = PriorityQueue()

for i in range(n):
    q = int(input())
    pq.put(q)

qw = []

while(pq.qsize() > 1):
    r = pq.get()
    f = pq.get()
    qw.append(r+f)
    pq.put(r+f)

print(sum(qw))