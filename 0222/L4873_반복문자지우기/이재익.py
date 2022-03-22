import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = input()
    NL = []
    for i in N:
        NL.append(i)
    # HW와 마찬가지로 무한 반복되는 while문과 break를 이용.
    while 1:
        cnt = 0
        for i in range(len(NL)-1):
            # 만약 이어지는 두 글자가 같은 글자라면,
            if NL[i] == NL[i+1]:
                # 두 글자의 값을 각각 #로 바꿔줌.
                NL[i] = '#'
                NL[i+1] = '#'
                cnt += 2
            # 만약 더 이상 연속되는 같은 글자가 없다면 종료
        if '#' not in NL:
            a = ''.join(NL)
            print(f'#{tc} {len(a)}')
            break
            # 만약 같은 글자가 있었다면, 제거하고 다시 루프 시작.
        for i in range(cnt):
            NL.remove('#')