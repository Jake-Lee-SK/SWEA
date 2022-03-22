import sys
sys.stdin = open('input.txt')


T=int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    leaf = [list(map(int, input().split())) for _ in range(M)]
    tree = [0]*(N+1)
    for i in range(M):
        tree[leaf[i][0]] = leaf[i][1]
    for i in range(len(tree)-1, 1, -1):
        if tree[i//2] == 0 and (i-1)//2 == i//2:
            tree[i//2] = tree[i-1] + tree[i]
        elif tree[i//2] == 0 and (i-1)//2 != i//2:
            tree[i//2] = tree[i]
    print(f'#{tc} {tree[L]}')