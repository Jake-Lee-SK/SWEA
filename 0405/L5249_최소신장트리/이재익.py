import sys
sys.stdin = open('input.txt')

# 프림 알고리즘

T = int(input())

for tc in range(1, T+1):
    N, E = map(int,input().split())
    # 트리에 가중치와 간선 정보를 저장함.
    tree = [[] for _ in range(N+1)]
    for i in range(E):
        A, B, C = map(int, input().split())
        tree[A].append([A, B, C])
        tree[B].append([B, A, C])
    mst = [] # 최저 가중치를 가지는 간선들을 저장할 장소
    nod_list = [] # 연결된 노드들을 저장할 장소
    nod_list.append(0) # 어디서 시작하든 상관 없으므로, 0번 노드부터 시작
    while len(nod_list) < N+1:
        min_nod = 10000000000000000000000000000000000000000000
        min_edge = []
        # 연결된 노드 집단 밖으로 가는 간선 중 가중치의 최솟값을 가지는 것을 찾음
        for i in nod_list:
            for j in range(len(tree[i])):
                if tree[i][j][2] < min_nod and tree[i][j][1] not in nod_list:
                    min_nod = tree[i][j][2]
                    min_edge = tree[i][j]
        # 간선을 찾았다면 간선 추가, 연결 노드에 노드 번호 추가
        mst.append(min_edge)
        nod_list.append(min_edge[1])
    # 간선들의 가중치를 더함
    sum_cnt = 0
    for i in range(len(mst)):
        sum_cnt += mst[i][2]
    print(f'#{tc} {sum_cnt}')