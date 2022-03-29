import sys
sys.stdin = open('input.txt')

move_x = [0,1]
move_y = [1,0]
def DFS(y, x, cnt):
    global max
    # 오른쪽 맨 밑에 다다르면 값을 반환하고, 만약 최솟값이라면 값을 저장
    if y==N-1 and x ==N-1:
        if cnt < max:
            max = cnt
        return
    # 진행하다가 이미 최솟값을 넘어서면 의미가 없으므로 뒤로 돌아갈 것
    if cnt > max:
        return
    # 방향은 오른쪽과 밑으로만 향하므로 그 방향으로만 깊이 탐색을 진행
    for i in range(2):
        new_y = y+move_y[i]
        new_x = x+move_x[i]
        if 0<=new_x <=N-1 and 0<=new_y<=N-1:
            # 그 다음으로 향하면서 그 다음번째 칸에 있는 값을 더함
            DFS(new_y, new_x, cnt+matrix[new_y][new_x])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for i in range(N)]
    # 생각할 수 있는 최댓값으로 설정
    max = 1000000000000000000000000000000000000000
    DFS(0, 0, matrix[0][0])
    print(f'#{tc} {max}')