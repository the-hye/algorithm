n = int(input())
data = set(map(int,input().split()))

find_n = int(input())
find_data = list(map(int,input().split()))

for i in find_data:
    if i in data:
        print(1)
    else:
        print(0)