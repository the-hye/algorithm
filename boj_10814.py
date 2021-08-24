n = int(input())
data = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    data.append((age, name))

data.sort(key= lambda x:x[0])

for i in range(n):
    print(data[i][0], data[i][1])
