import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    L = input()
    # Stack 형식 이용
    stack = [] # '{'을 1로, '('을 2로 저장
    error = 0
    for i in L:
        if i == '{':
            stack.append(i)
        if i == '(':
            stack.append(i)
        if i == '}':
            # 만약 스택 맨 끝에 저장된 것이 '{'라면 그것을 제거하고,
            # 스택이 비었거나 '{'가 아니라면 오류 발생
            if len(stack)==0:
                error += 1
                break
            if stack.pop() != '{':
                error += 1
        if i == ')':
            # 만약 스택 맨 끝에 저장된 것이 '('라면
            # 그것을 제거하고, 아니라면 오류 발생 +1
            if len(stack)==0:
                error += 1
                break
            if stack.pop() != '(':
                error += 1
    # 스택에 아직 남아있는 숫자가 있으면 오류있는 것
    if stack:
        error += 1

    if error > 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
