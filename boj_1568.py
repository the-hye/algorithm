n = int(input())
time = 0
k = 1

while n>0:
    if n < k:
        k =1
    n -= k
    time += 1
    k += 1

print(time)
