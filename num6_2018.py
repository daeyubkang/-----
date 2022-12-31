n = int(input())
count = 1
start = 1
end = 1
sum = 1

while(end<n) :
    if(sum == n):
        count += 1
        end += 1
        sum = sum + end
    elif(sum > n):
        sum = sum - start
        start += 1
    else:
        end +=1
        sum = sum + end

print(count)