def counting(tropies):
    now_max = tropies[0]
    count = 1
    for i in tropies:
        if i > now_max:
            count += 1
        now_max = max(i, now_max)
    return count

n = int(input())
tropies = []

for _ in range(n):
    trophy = int(input())
    tropies.append(trophy)

print(counting(tropies))
tropies.reverse()
print(counting(tropies))

