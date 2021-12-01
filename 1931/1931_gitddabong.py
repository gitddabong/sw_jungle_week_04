import sys
input = sys.stdin.readline

n = int(input())
discuss = []
for _ in range(n):
    start, end = map(int, input().split())
    discuss.append([start, end])

discuss.sort(key= lambda x : (x[1], x[0]))
# 10번 라인과 아래 두 줄은 같은 동작
# discuss.sort(key= lambda x : x[0])
# discuss.sort(key= lambda x : x[1])
print(discuss)

cnt = 0
last_end = 0
for start, end in discuss:
    if last_end > start:
        continue
    else:
        cnt += 1
        last_end = end

print(cnt)