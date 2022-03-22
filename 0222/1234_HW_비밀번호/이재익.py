import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    list = []
    N, L = input().split()
    # L을 str형태로 받아왔으므로 list 안에 하나씩 저장.
    NL = []
    for i in range(int(N)):
        NL.append(L[i])
    # 무한 반복되는 while문과 break를 이용.
    while 1:
        cnt = 0
        for i in range(len(NL)-1):
            # 만약 이어지는 두 수가 같은 수라면,
            if NL[i] == NL[i+1]:
                # 두 수를 각각 #를 추가함.
                NL[i] = '#'
                NL[i+1] = '#'
                cnt += 2
            # 만약 더 이상 연속되는 같은 수가 없다면 종료
        if '#' not in NL:
            a = ''.join(NL)
            print(f'#{tc} {a}')
            break
            # 만약 같은 수가 있었다면, 제거하고 다시 루프 시작.
        for i in range(cnt):
            NL.remove('#')