import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    # target 인덱스를 만들기 위해 필요한 동전의 경우의 수를 모두 저장한 리스트
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1   # 이전 값을 바탕으로 다음 값을 갱신하니까 0이 아닌 1?
    for i in coins:     # 동전 
        for j in range(1, target + 1):
            if j >= i:      # 동전 단위가 target보다 클 경우
                dp[j] += dp[j - i]
    print(dp[target])