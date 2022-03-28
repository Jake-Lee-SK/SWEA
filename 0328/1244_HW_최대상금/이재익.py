import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = input().split() # N = 기본 숫자, M  = 교환 횟수
    # 교환 횟수를 숫자로 변환
    M = int(M)
    # 기본 숫자의 길이를 저장
    length = len(N)
    # 맨 처음 숫자를 now에 set 형식으로 저장
    now = set([N])
    # next에 모든 경우의 수를 저장할 것
    next = set()
    for _ in range(M):
        # now에 있는 모든 경우의 숫자가 빠질 때 까지
        while now:
            # now에 있는 것을 하나 빼서
            s = now.pop()
            # 리스트화 시킨 다음에
            s = list(s)
            # 그 리스트에 있는 숫자를 모두 한번씩 바꾸는 경우의 수를 next에 저장함
            for i in range(length):
                for j in range(i+1, length):
                    s[i], s[j] = s[j], s[i]
                    next.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        # 그리고 저장한 next를 now로 바꿔줌.
        now, next = next, now
    print(f'#{tc} {max(now)}')