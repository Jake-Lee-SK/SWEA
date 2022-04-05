import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = []
    matrix = []
    # 섬 사이의 거리^2 * 세율로 값을 저장
    tmp_X = list(map(int, input().split()))
    tmp_Y = list(map(int, input().split()))
    tax = float(input())
    for i in range(N):
        matrix.append([tmp_X[i], tmp_Y[i]])
    # 무방향 간선으로 저장
    for i in range(N):
        for j in range(i+1, N):
            graph.append([((matrix[j][1] - matrix[i][1]) ** 2 + (matrix[j][0] - matrix[i][0]) ** 2) * tax, i, j])
            graph.append([((matrix[j][1] - matrix[i][1]) ** 2 + (matrix[j][0] - matrix[i][0]) ** 2) * tax, j, i])
    # 거리 순으로 정렬
    graph.sort()
    mst = []
    nod = [graph[0][1]]
    while len(nod) != N:
        # 거리가 가장 가까우면서 nod에서 갈 수 있는 최저값을 계속 탐색(sort되어있으므로 순서대로임)
        for i in range(len(graph)):
            if graph[i][2] not in nod and graph[i][1] in nod:
                nod.append(graph[i][2])
                mst.append(graph[i])
                break
    cnt = 0
    for i in range(len(mst)):
        cnt += mst[i][0]
    print(f'#{tc} {round(cnt)}')