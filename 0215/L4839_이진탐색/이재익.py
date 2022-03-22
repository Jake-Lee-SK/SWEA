import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    P, A, B = list(map(int, input().split()))
    Ap = 0
    Bp = 0
    start = 1
    end = 0
    A_cnt = 0
    B_cnt = 0
    # A 찾기
    while 1:
        if A_cnt == 0:
            end = P
        Ap = int((start+end)/2)
        if Ap > A: # 찾는 페이지가 왼쪽에 있다면
            end = Ap
            A_cnt += 1
        if Ap < A: # 찾는 페이지가 오른쪽에 있다면
            start = Ap
            A_cnt += 1
        if Ap+1 == A and A == P: # 찾는 페이지가 P의 오른쪽 끝과 같다면
            A_cnt += 1
            start = 1
            end = 0
            break
        if Ap == A: # 페이지를 찾았다면
            A_cnt += 1
            start = 1
            end = 0
            break
    # B 찾기
    while 1:
        if B_cnt == 0:
            end = P
        Bp = int((start + end) / 2)
        if Bp > B: # 찾는 페이지가 왼쪽에 있다면
            end = Bp
            B_cnt += 1
        if Bp < B: # 찾는 페이지가 오른쪽에 있다면
            start = Bp
            B_cnt += 1
        if Bp+1 == B and B == P: # 찾는 페이지가 P의 오른쪽 끝과 같다면
            B_cnt += 1
            start = 1
            end = 0
            break
        if Bp == B: # 페이지를 찾았다면
            B_cnt += 1
            break

    if A_cnt < B_cnt:
        print(f'#{tc} A')
    if A_cnt == B_cnt:
        print(f'#{tc} 0')
    if A_cnt > B_cnt:
        print(f'#{tc} B')
