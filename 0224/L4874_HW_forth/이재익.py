import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    l = list(map(str, input().split()))
    stack = [] # 숫자를 저장할 stack 리스트
    left = 0 # 왼쪽에 있는 숫자
    right = 0 #오른쪽에 있는 숫자
    for i in range(len(l)):
        if i == len(l)-1: # 마지막에 이르렀을 때
            if l[i] == '.' and len(stack) == 1: # 마지막 인자가 '.'이고, stack에 있는 숫자가 1개라면
                print(f'#{tc} {stack[0]}') #정상이므로 출력
                break
            else:
                print(f'#{tc} error') # 마지막 인자가 '.'이 아니거나, stack에 있는 숫자가 1개가 아니라면 오류
                break

        if l[i] != '+' and l[i] != '-' and l[i] != '*' and l[i] != '/' and l[i] != '.':
            stack.append(l[i]) # 숫자면 스택에 저장
        else:
            if len(stack) >= 2: # 연산자를 만났을 경우, 2개 이상 쌓인 스택 숫자에 대해서 계산
                if l[i] == '+':
                    right = int(stack.pop())
                    left = int(stack.pop())
                    stack.append(left+right)
                if l[i] == '-':
                    right = int(stack.pop())
                    left = int(stack.pop())
                    stack.append(left-right)
                if l[i] == '*':
                    right = int(stack.pop())
                    left = int(stack.pop())
                    stack.append(left*right)
                if l[i] == '/':
                    right = int(stack.pop())
                    left = int(stack.pop())
                    stack.append(left//right)
            else: # 스택에 쌓여있는 숫자가 2개 미만일 경우
                print(f'#{tc} error')
                break