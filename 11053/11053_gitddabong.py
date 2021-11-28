import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [0 for _ in range(n)]
max_val = 0
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:   # 현재 보고있는 숫자가 큰데 체크리스트에서는 수가 작은 경우
            dp[i] = dp[j]
    dp[i] += 1
    max_val = max(max_val, dp[i])

print(max_val)

# n = int(input())
# nums = list(map(int, input().split()))
# dp = [0 for i in range(n)]
# for i in range(n):
#     for j in range(i):  
#         if nums[i] > nums[j] and dp[i] < dp[j]:     # 
#             dp[i] = dp[j]
#     dp[i] += 1
# print(max(dp))