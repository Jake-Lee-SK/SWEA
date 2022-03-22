import sys
sys.stdin = open('input.txt')

T = 10

def my_max(list):
    cnt = 0
    for i in range(len(list)):
        if cnt < list[i]:
            cnt = list[i]
    return cnt

for tc in range(1, 11):
    A = int(input())
    BD = list(map(int, input().split()))
    cnt = 0
    for i in range(2, A-2):
        first = BD[i-2]
        second = BD[i-1]
        main = BD[i]
        third = BD[i+1]
        forth = BD[i+2]
        BDs = [first, second, third, forth]
        if main > my_max(BDs):
            cnt += main - my_max(BDs)
    print(f'#{tc} {cnt}')

