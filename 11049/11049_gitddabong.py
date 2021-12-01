import sys
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
dp =[[0 for _ in range(n)] for _ in range(n)] 

# for i in range(1, n): #몇 번째 대각선?
#     for j in range(0, n-i): #대각선에서 몇 번째 열?
    
#         if i == 1: #차이가 1밖에 나지 않는 칸
#             dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
#             continue
        
#         dp[j][j+i] = 2**32 #최댓값을 미리 넣어줌
#         for k in range(j, j+i): 
#             dp[j][j+i] = min(dp[j][j+i], 
#                             dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])

# print(dp[0][n-1]) #맨 오른쪽 위

for j in range(1, n):
    for i in range(j-1, -1, -1):

        if j - i == 1:
            dp[i][j] = matrix[i][0] * matrix[i][1] * matrix[j][1]
            continue

        dp[i][j] = 2**32
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], 
                            dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
print(dp[0][n-1])