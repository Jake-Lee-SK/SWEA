import sys
sys.stdin = open('input.txt')

# 콤비네이션 이용
from itertools import combinations

for tc in range(1, int(input())+1):
    # N = NxN의 크기
    # M = 캐는 벌통의 크기
    # C = sum(벌통)의 최대치

    N, M, C = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 꿀을 캔 최대치를 저장하는 곳
    honeys = []
    for i in range(N):
        for j in range(N-M+1):
            # C 넘으면 제외하고, 제일 큰 값까지만 고려할 것
            if sum(matrix[i][j:j+M]) > C:
                max_sets = 0
                pick_sets = ()
                imsi = 0
                # 벌통 채취 구간 안에 있는 모든 숫자를 경우의 수를 따짐
                for k in range(1, M):
                    subset = list(combinations(matrix[i][j:j+M], k))
                    for sets in subset:
                        # 만약 경우의 수의 합이 C보다 작거나 같으면
                        if sum(sets) <= C:
                            notes = 0
                            # 경우의 수 각각의 제곱을 더해보고
                            for n in sets:
                                notes += n**2
                            # 그 제곱의 합이 최대가 되는 값을 저장함
                            if notes > max_sets:
                                max_sets = notes
                # 제곱 합의 최대치를 벌통 채취 구간의 꿀 채취 최대치로 추가함.
                honeys.append(max_sets)
            # 합계가 C를 안넘는다면 그냥 제곱값들의 합을 채취 최대치로 추가함
            else:
                imsi = 0
                for k in range(M):
                    imsi += matrix[i][j+k]**2
                honeys.append(imsi)
    max_cnt = 0
    # 만약 채취 구간이 1이거나 가로 한 칸 전체면 별 의미 없으므로 combinations 돌린 후 최대치를 반환
    if M == 1 or M == N:
        imsi = list(combinations(honeys, 2))
        for i in range(len(imsi)):
            if max_cnt < sum(imsi[i]):
                max_cnt = sum(imsi[i])
    # 채취 구간이 1<채취구간<가로 한칸 크기면 제외를 해줘야 하므로 제외하는 식 구현
    else:
        for i in range(N):
            for j in range(N-M+1):
                # honeys를 건들 수 없으므로 임시 리스트에 honeys 값을 복사함.
                imsi = honeys[:]
                # hoenys의 (N-M+1)*i+j번째 값이 합계 최대값을 가지는 지 계산하기 위함
                imsi2 = (N-M+1)*i+j
                imsi3 = []
                # 만약 i번째 가로 안에서 겹치는 칸이 있다면 제외해주기 위한 식
                for k in range(1, M):
                    if imsi2+k<(N-M+1)*(i+1):
                        imsi3.append(imsi2+k)
                    if (N-M+1)*i<=imsi2-k:
                        imsi3.append(imsi2-k)
                # 겹치는 곳이 있다면 임시 리스트에서 0으로 만들어버림
                for k in imsi3:
                    imsi[k] = 0
                # 겹치는 곳을 제외했으므로, 나머지 칸 중 최댓값을 갖는 경우의 수를 계산
                for k in range(len(imsi)):
                    if k != imsi2 and max_cnt < imsi[k] + imsi[imsi2]:
                        max_cnt = imsi[k] + imsi[imsi2]
    print(f'#{tc} {max_cnt}')