import sys
input = sys.stdin.readline

n, target = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

count = 0
for coin in coins:
    if target == 0:
        break

    count += target // coin
    target = target % coin

print(count)