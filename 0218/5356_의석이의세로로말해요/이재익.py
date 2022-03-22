import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = [list(input()) for _ in range(5)]
    M = []
    A = []
    # 어떤 row는 col의 크기가 다르다.
    for i in range(5):
        M.append(len(N[i]))

    for i in range(5):
        if len(N[i]) < max(M):
            for j in range(max(M)-len(N[i])):
                N[i].append('#')
        else:
            continue

    for i in range(max(M)):
        for j in range(5):
            A.append(N[j][i])
    if '#' in A:
        for i in range(A.count('#')):
            A.remove('#')
    print(f'#{tc}', end=' ')
    print(''.join(A))
