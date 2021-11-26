import sys
input = sys.stdin.readline

n = int(input())
tiles = [1 for _ in range(n+2)]
tiles[1] = 2
for i in range(2, n+2):
    tiles[i] = ((tiles[i-2] % 15746) + (tiles[i-1] % 15746)) % 15746

print(tiles[n-1])