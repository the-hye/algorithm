from collections import deque

test_case = int(input())

for _ in range(test_case):
    n, m = map(int,input().split())
    queue = deque(map(int,input().split()))

    index = [0 for i in range(n)]
    index[m] = 1
    count = 0

    while True:
        if queue[0] == max(queue):
            if index[0] == 1:
                break
            else:
                queue.popleft()
                index.pop(0)
                count += 1
        else:
            queue.append(queue.popleft())
            index.append(index.pop(0))
    print(count + 1)


    



