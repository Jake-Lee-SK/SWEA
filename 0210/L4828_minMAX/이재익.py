import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    min_num = numbers[0]
    max_num = 0
    for idx in range(N):
        if min_num > numbers[idx]:
            min_num = numbers[idx]
        else:
            continue
    for idx in range(N):
        if numbers[idx] > max_num:
            max_num = numbers[idx]
        else:
            continue
    answer = max_num - min_num


    print(f'#{TC} {answer}')