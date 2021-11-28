import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    coins = list(map(int, input().split()))
    amount = int(input())

    # target 인덱스를 만들기 위해 필요한 동전의 경우의 수를 모두 저장한 리스트
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1   # 이전 값을 바탕으로 다음 값을 갱신하니까 0이 아닌 1?
    for coin in coins:     # 동전 
        for idx in range(1, amount + 1):
            if idx >= coin:      # 동전 단위가 현재 amount보다 클 경우
                dp[idx] += dp[idx - coin]      # 현재 amount에서 동전 단위만큼 뺀 수를 만들 수 있는 가짓수를 현재 수의 경우의 수에 더함
    print(dp[amount])