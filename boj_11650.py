import sys

n = int(input())
data = []

for _ in range(n):
    x, y = list(map(int,sys.stdin.readline().split()))
    data.append((x, y))

data.sort()

for i in data:
    print(i[0], i[1])
