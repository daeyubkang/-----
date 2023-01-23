import math

n = int(input())

result = n

for i in range(2,int(math.sqrt(n))+1):
    if n%i ==0:
        result = result - result//i
        while(n%i==0):
            n = n//i

if n > 1:
    result = result - result//n

print(result)



# count = 0
# a = [0]*1000001
# a[1] = 1
# for i in range(2,int(math.sqrt(n))+1):
#     if a[i] != 0:
#         continue
#     for j in range(i,int(math.sqrt(n))//i+1):
#         a[i*j] = 1

# qwe = []

# for i in range(2,int(math.sqrt(n))+1):
#     if n%i==0:
#         qwe.append(i)

# for i in range(len(qwe)):
#     qw = qwe[i]
#     if a[qw] == 1 and n//qw != int(math.sqrt(n//qw))**2:
#         qwe[i] = n//qw
    

# qwe.sort()

# if len(qwe) ==0:
#     result = result - 1

# for i in qwe:
#     result = result - result//i
    

# print(result)