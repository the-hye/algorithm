n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
length = len(cards)

for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_cards = cards[i] + cards[j] + cards[k]
            if sum_cards <= m:
                result = max(result, sum_cards)

print(result)
