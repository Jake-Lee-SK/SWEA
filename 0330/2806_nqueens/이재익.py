import sys
sys.stdin = open('input.txt')


def dfs(col):
    global cnt
    # 끝까지 갔다면 cnt를 +1
    if col == N:
        cnt += 1
        return

    for i in range(N):
        # 만약 방문하지 않은 곳이라면
        if visited[i] == 0:
            queen[col] = i  # 퀸을 올린다고 가정.
            # 퀸을 올렸을 때
            if check(col):
                visited[i] = 1
                dfs(col + 1)
                visited[i] = 0
def check(M):
    for i in range(M):
        if (queen[i] == queen[M]) or (M-i == abs(queen[M] - queen[i])):
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    queen = [0] * N
    visited = [0] * N
    cnt = 0
    dfs(0)
    print(f'#{tc} {cnt}')