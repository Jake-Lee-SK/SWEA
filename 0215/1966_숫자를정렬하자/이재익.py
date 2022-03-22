import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Numbers = list(map(int, input().split()))


    # 1 버블 sort

    for i in range(N): # 0번부터, N-1번까지 반복
        for j in range(N-i-1): # 0번부터, N-i-1(첫 값은 N-1)번까지 진행.
            if Numbers[j] > Numbers[j+1]: # idx j 값이 그 다음 값보다 크면
                Numbers[j], Numbers[j+1] = Numbers[j+1], Numbers[j]
                # 서로 위치를 바꿔줌.
                # 이러한 행위를 i번 만큼 반복해주면, sorting이 됨.

    print(f'#{tc}', end=' ')
    for i in range(N):
        print(Numbers[i], end=' ')
    print()

    # 2 카운팅 sort

    after_counting = [] # 카운팅 후의 리스트(print 할 리스트)
    count_li = [0 for _ in range(max(Numbers)+1)]
    # 0으로 채워 놓은 카운팅 리스트
    for i in Numbers:
        count_li[i] += 1
    # 카운팅 리스트의 index 자리에 빈도만큼 1을 증가시킴.

    for i in range(len(count_li)):
        num = count_li[i] # 있는 자리에 있는 숫자를 따로 저장
        for k in range(num): # 만약 num = 0이면 넘어감
            after_counting.append(i)
            # num > 0이면 num만큼 i를 추가시킴

    print(f'#{tc}', end=' ')
    for i in range(N):
        print(after_counting[i], end=' ')
    print()

    # 3 선택정렬

    for i in range(N-1):
        min_idx = i # i를 가장 작은 숫자라고 가정
        for j in range(i+1, N):
            if Numbers[j] < Numbers[min_idx]: # 만약 그 다음 숫자가 i보다 크면,
                # min_idx를 그 다음 숫자로 변경.
                min_idx = j
        Numbers[i], Numbers[min_idx] = Numbers[min_idx], Numbers[i]
        # i번째 idx에 해당하는 숫자와, j번째(혹은 i번째) 인덱스를 서로 위치를 바꿔줌.
        # 그것을 반복하면, 위치가 계속 바뀌면서 정렬이 됨.

    print(f'#{tc}', end=' ')
    for i in range(N):
        print(Numbers[i], end=' ')
    print()