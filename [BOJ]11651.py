import time

# x 와 y 위치 switch
def change(x):
    for i in range(N):
        result[i][0], result[i][1] = result[i][1], result[i][0]

# 최대힙 생성
def heap(list):
    for i in range(len(list)):
        c = i
        while c > 0:
            root = (c-1)//2
            if list[c][0] > list[root][0]:
                list[c],list[root] = list[root],list[c]
            elif list[c][0] == list[root][0]:
                if list[c][1] > list[root][1]:
                    list[c], list[root] = list[root], list[c]
            c = root


# 힙 정렬
def heapsort(list):
    heap(list)
    for i in range(len(list)-1, -1, -1):
        list[0], list[i] = list[i], list[0]
        root = 0
        c = 0
        while(c < i):
            c = (2 * root) + 1
            if c < i-1 and list[c][0] < list[c+1][0]:
               c += 1
            elif c < i-1 and list[c][0] == list[c+1][0]:
                if list[c][1] < list[c+1][1]:
                    c += 1
            if c < i and list[root][0] < list[c][0]:
                list[root], list[c] = list[c], list[root]
            elif c < i and list[root][0] == list[c][0]:
                if list[root][1] < list[c][1]:
                    list[root], list[c] = list[c], list[root]
            root = c

# read file
f = open('file name')

# 총 좌표의 개수
N = int(f.readline())

# 결과 저장 리스트
result = []

# make list
for i in range(N):
    result.append(f.readline().split())

start = time.time()
# x,y 좌표 변경
change(result)
# 정렬
heapsort(result)
# x 와 y 위치 switch
change(result)
# 수행 시간
print("수행시간 : ", time.time()-start)

# 결과출력
for i in range(N):
    print(i+1,":",result[i][0],result[i][1])


