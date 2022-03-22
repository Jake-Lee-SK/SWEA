import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = 0 # 2
    b = 0 # 3
    c = 0 # 5
    d = 0 # 7
    e = 0 # 11
    while 1:
        if N % 2 == 0: #2로 나눴을 때 나머지가 X
            N = int(N/2)
            a += 1
        else:
            break
    while 1:
        if N % 3 == 0: #2로 나눴을 때 나머지가 X
            N = int(N/3)
            b += 1
        else:
            break
    while 1:
        if N % 5 == 0: #2로 나눴을 때 나머지가 X
            N = int(N/5)
            c += 1
        else:
            break
    while 1:
        if N % 7 == 0: #2로 나눴을 때 나머지가 X
            N = int(N/7)
            d += 1
        else:
            break
    while 1:
        if N % 11 == 0: #2로 나눴을 때 나머지가 X
            N = int(N/11)
            e += 1
        else:
            break

    print(f'#{tc} {a} {b} {c} {d} {e}')