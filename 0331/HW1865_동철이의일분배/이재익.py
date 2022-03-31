import sys
sys.stdin = open('input.txt')

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤ N ≤ 16)이 주어진다.
# 다음 N개의 줄의 i번째 줄에는 N개의 정수 Pi, 1, … , i, N(0 ≤ Pi, j ≤ 100)이 주어진다.
# Pi, j는 i번 사람이 j번 일을 성공할 확률을 퍼센트 단위로 나타낸다.

def DFS(cnt, value):
    global max_value
    if cnt == N:
        if value > max_value:
            max_value = value
        return
    if cnt != N-1 and value <= max_value:
        return

    for i in range(N):
        if check[i] == False:
            check[i] = True
            a = value * M[cnt][i]/100
            DFS(cnt+1, a)
            check[i] = False

for tc in range(1, int(input())+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    check = [False]*N
    max_value = 0
    DFS(0, 1)
    b = max_value*100
    print(f'#{tc} {"%.6f" %b}')