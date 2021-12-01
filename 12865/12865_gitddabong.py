# import sys
# input = sys.stdin.readline

# n, w_limit = map(int, input().split())

# things = []
# # [무게, 가치]
# for _ in range(n):
#     things.append(list(map(int, input().split())))
# things.sort()

# dp = [0 for _ in range(w_limit+1)]
# for weight, value in things:
#     dp[0] = value
#     for j in range(1, w_limit+1):
#         if j >= weight:
#             pass
#             # 이 부분이 문제같은데..
#             # dp[j] += dp[j - weight]

# print(dp[-1])



# 이 문제 1차원 리스트로 풀이 가능

# import sys

# input = sys.stdin.readline
# N, K = map(int, input().split())    # 물건 개수, 무게 제한
# stuff = [[0,0]]     # 물건의 무게와 가치를 담은 리스트
# knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]    # 2차원 리스트에서 비용 정리

# for _ in range(N):
#     stuff.append(list(map(int, input().split())))

# # 냅색 문제 풀이
# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         weight = stuff[i][0]
#         value = stuff[i][1]

#         if j < weight:
#             knapsack[i][j] = knapsack[i - 1][j] # weight보다 작으면 위의 값을 그대로 가져온다
#         else:
#             knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

# print(knapsack[N][K])

import sys
input = sys.stdin.readline

N, W = map(int, input().split())

stuff = []
for _ in range(N):
    stuff.append(list(map(int, input().split())))

knapsack = [0 for _ in range(W+1)]
for weight, value in stuff:
    for i in range(W, 0, -1):
        if i < weight:
            continue
        
        knapsack[i] = max(knapsack[i], knapsack[i-weight] + value, knapsack[i-1])
print(knapsack[-1])