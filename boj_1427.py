data = input()
array = [int(n) for n in data]

order = sorted(array, reverse=True)

for j in order:
    print(j, end="")
