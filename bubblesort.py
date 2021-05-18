import time

# 내림차순 정렬 함수
def sortRank(x):
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            if x[i] < x[j]:
                x[i], x[j] = x[j], x[i]

# read file
f = open('file name')

# R, N, S 추출 및 데이터 정리
data = f.readline().split(', ')  # , 기준 split
data = [word.strip(')\n').strip('(') for word in data]  # 괄호와 엔터 제거
R = int(data[0])  # 10000
N = int(data[1])  # 5000
S = []
for i in range(2, len(data)):
    S.append(data[i])
S = list(map(int, S))

# 기존 랭킹 R개 입력
ranking = []
for i in range(R):
    score = f.readline().split(' ')[1]  # 띄어쓰기 기준 split
    ranking.append(int(score))

# ranking 내림차순
sortRank(ranking)
# N개로 ranking 수정
ranking = ranking[:N]

start = time.time()
# S 순위 추출
for i in S:
    # S[i]이 ranking의 마지막 값보다 작을 때 -> 순위권 밖
    if i < ranking[-1]:
        print("Score", i, ": -1")
    # 순위권 안 : ranking에 입력 후 재정렬
    else:
        ranking.append(i)
        sortRank(ranking)
        print("Score", i, ":", ranking.index(i)+1)

# 수행시간
print("수행시간 : ", time.time()-start)
