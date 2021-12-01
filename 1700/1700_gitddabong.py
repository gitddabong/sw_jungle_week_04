import sys
input = sys.stdin.readline

N, K = map(int, input().split())
orders = list(map(int, input().split()))
multitap = [0] * N
swap = 0    # 꽂혀있다가 빼야 될 전자제품의 번호
max_I = 0   # 꽂혀 있는 전자제품 중 가장 나중에 쓰게 될 전자제품의 인덱스
cnt = 0
for i in range(K):
    # 멀티탭에 해당 전기용품이 꽂혀있는 경우
    if orders[i] in multitap:
        continue

    # 멀티탭에 빈 구멍이 있는 경우
    elif 0 in multitap:
        multitap[multitap.index(0)] = orders[i]

    # 멀티탭에 빈 공간이 없는 경우
    else:
        left = orders[i:]
        for elec in multitap:   # elec : 현재 멀티탭에 장착된 전기제품
            # 멀티탭에 꽂혀 있는 전기용품 중 이후로 사용하는 것이 없는 경우
            if elec not in left:
                swap = elec     # 사용하지 않는 전기용품 중 어느것이라도 괜찮으니까 맨 먼저 찾는 전기용품 
                break

            # 멀티탭에 꽂혀 있는 전기용품 중 이후로 사용하는 것이 있는 경우
            # 꽂혀 있는 전기용품 중 가장 나중에 쓰는 전기용품 빼기

            # 이후에 남은 전기용품 중에서 가장 나중에 쓰는 전기용품의 인덱스 가져오기
            # 무슨 전기용품인지는 저장 안해도 됨. 어차피 그 인덱스 접근하면 되니까
            elif left.index(elec) > max_I:
                max_I = left.index(elec)    # max인덱스 값 갱신
                swap = elec                 # swap이라는 변수에 잔기용품 번호 저장
        multitap[multitap.index(swap)] = orders[i]  # 멀티탭 자리에 바꿀 전기용품 빼고 새 전기용품 장착
        max_I = swap = 0    # 변수 초기화
        cnt += 1
print(cnt)

