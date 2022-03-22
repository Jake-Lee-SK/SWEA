import sys
sys.stdin = open('input.txt')

def find(number): # 연속해서 탐색해나갈 함수 생성
    global stack
    global left
    global right
    stack.append(number) # 노드를 스택에 추가
    if number in left: # 왼쪽에 있으면 탐색
        find(left[number])
    if number in right: # 오른쪽에 있으면 탐색
        find(right[number])
    elif number not in left and number not in right: # 없으면 멈추기
        return

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    M = list(map(int, input().split()))
    left = {}
    right = {}
    for i in range(E): # 왼쪽과 오른쪽 자식 노드를 동시에 저장
        if M[2*i] in left:
            right[M[2*i]] = M[2*i+1]
        else:
            left[M[2*i]] = M[2*i+1]
    stack = []
    find(N)
    print(f'#{tc} {len(stack)}')