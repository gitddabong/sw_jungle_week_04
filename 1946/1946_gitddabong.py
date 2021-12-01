# import sys
# input = sys.stdin.readline

# testcase = int(input())
# for _ in range(testcase):
#     n = int(input())
#     ranks = []
#     for _ in range(n):
#         ranks.append(list(map(int,input().split())))

#     # phase 1
#     ranks.sort(key= lambda x : (x[0]))
#     top1 = ranks[0][0]
#     top2 = ranks[0][1]
    
#     for i in range(1, len(ranks)):
#         if top1 < ranks[i][0] and top2 < ranks[i][1]:
#             ranks[i] = 0
#     while 0 in ranks:
#         ranks.remove(0)

#     # phase 2
#     ranks.sort(key= lambda x : (x[1]))
#     top1 = ranks[0][0]
#     top2 = ranks[0][1]
    
#     for i in range(1, len(ranks)):
#         if top1 < ranks[i][0] and top2 < ranks[i][1]:
#             ranks[i] = 0
#     while 0 in ranks:
#         ranks.remove(0)

#     print(len(ranks))

import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    ranks = []
    for _ in range(n):
        ranks.append(list(map(int,input().split())))

    ranks.sort()
    cnt = 1
    min = ranks[0][1]   # 서류 1등의 면접 순위
    
    for i in range(1, n):
        if ranks[i][1] < min:
            min = ranks[i][1]
            cnt += 1
    print(cnt)