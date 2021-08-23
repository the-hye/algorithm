test_case = int(input())

for _ in range(test_case):
    left = []
    right = []
    data = input()

    for i in data:
        if i == '>':
            if right:
                left.append(right.pop())
        elif i == '<':
            if left:
                right.append(left.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    print("".join(left)+"".join(reversed(right)))
    
                