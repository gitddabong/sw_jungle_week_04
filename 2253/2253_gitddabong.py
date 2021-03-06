# import sys
# input = sys.stdin.readline

# length, n = map(int, input().split())
# dp = [0 for _ in range(length + 1)]
# for _ in range(n):
#     idx = int(input())
#     dp[idx] = -1

# dp[2] = 1
# jump = 1
# for i in range(3, length+1):    # 2부터 length+1 인덱스까지 값 설정
#     # jump + 1 만큼 뛰어보고 그 인덱스에 값 갱신

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)]  # 속도를 행으로 사용
dp[1][0] = 0    # 초기값. 위치1은 점프 횟수가 0이니까 맞는 말이긴 해

stone_set = set()   # 돌의 위치가 중복되는 반례도 있나?
for _ in range(M):
    stone_set.add(int(sys.stdin.readline()))

for i in range(2, N + 1):   # 0행 인덱스는 빈 인덱스, 인덱스값은 각각의 위치
    if i in stone_set:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1): # 점프는 1부터. i를 이용해 점프 가능한 최댓값을 구하고 그 범위만큼 반복하면서 값 갱신
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))