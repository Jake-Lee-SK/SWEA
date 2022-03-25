import sys
sys.stdin = open('input.txt')

# 배열 순회하는 사각형
# 방향을 3번 꺾은 후에, 돌아오게 되면 정답
# 방향을 4번 꺾거나, 중간에 같은 대상을 만나게 되면 실패.
# 이 경우는 성공하는 것 중에 최대값만을 return하게 되어 있음
# 성공하지 못한다면 -1을 반환하게 됨.

directions = [(1,1), (1,-1), (-1,-1), (-1, 1)]

# y, x는 현재 좌표
# n은 꺾은 방향 갯수, cnt는 디저트
def DFS(y, x, n, cnt):
    global ans
    # 만약 방향을 꺾지 않았다면, 다음 것까지 배열 순회
    # 만약 n=0(한번도 꺾지 않음)~n=2(2번 꺾음)이면, 다음 방향을 제시함(n+2면, n, n+1까지 설정할 수 있으므로)
    # 만약 n=3(3번 꺾었다)이면, 다음 방향은 없음. 정답 아니면 실패한 것.

    if n<3:
        temp = n + 2
    else:
        temp = n + 1

    # 전환하는 방향을 설정
    for k in range(n, temp):
        ni = y+directions[k][0]
        nj = x+directions[k][1]

        if start[0] == ni and start[1] == nj: # 처음으로 다시 돌아왓다면
            ans = max(ans, cnt)
            return
        if 0 <= ni < N and 0<= nj < N:
            if visited[M[ni][nj]] == False: # 아직 방문하지 않았던 갯수의 디저트라면 진행
                visited[M[ni][nj]] = True # 갔던 곳으로 표기
                DFS(ni, nj, k, cnt+1)
                visited[M[ni][nj]] = False # 초기화

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    visited = [False]*101
    for i in range(N):
        for j in range(N):
            start = (i, j)
            visited[M[i][j]] = True # 방문했음
            DFS(i,j,0,1)
            visited[M[i][j]] = False # 초기화
    print(f'#{tc} {ans}')