# import sys 
# S1 = sys.stdin.readline().strip().upper() 
# S2 = sys.stdin.readline().strip().upper() 
# len1 = len(S1) 
# len2 = len(S2) 
# matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
# for i in range(1, len1 + 1):
#     for j in range(1, len2 + 1):
#         if S1[i - 1] == S2[j - 1]:
#             matrix[i][j] = matrix[i - 1][j - 1] + 1
#         else:
#             matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

# # print(matrix[-1][-1])
# print(matrix)

import sys
input = sys.stdin.readline
string1 = list(input().rstrip())
string2 = list(input().rstrip())
len1 = len(string1)
len2 = len(string2)

matrix = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
for i in range(1, len1+1):
    for j in range(1, len2+1):

        # 일치하는 알파벳을 찾았을 경우 각각의 알파벳이 추가되기 전 스트링에서 +1
        # 예를 들어 CAPC와 AC를 비교 중이었다면, 그 전의 스트링인 CAP와 A의 카운트값을 가져와서 +1
        if string1[i - 1] == string2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        # 알파벳이 일치하지 않을 경우 왼쪽이나 위 값 중에서 최댓값을 가져와 설정
        # 그 값이 왼쪽 값일지 윗 값일지는 알 수 없지만
        # 겹치는 문자열은 계속 그 성질이 유지되어야 하기 때문에 최댓값으로 가져옴
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])

