import sys
sys.stdin = open('input.txt')

def inorder(idx):
    global number

    if idx > N:
        return
    inorder(idx*2) # 왼쪽 끝까지 탐색
    # 탐색 후 끝을 찾으면
    tree[idx] = number # 노드에 값을 부여(부여한 후에는 1씩 증가)
    number += 1
    inorder(idx*2+1) # 오른쪽 탐색

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1) # 0번도 포함하므로 정점의 갯수보다 하나 더 많게 설정해야
    number = 1 # 노드에 부여하는 값 초기화
    inorder(1) # 이진 탐색트리 생성
    print(f'#{tc} {tree[1]} {tree[N//2]}')

#     stack = []
#     for i in range(N):
#         if i % 2 == 0: # 짝수
#             if i == 0 or i == 2:
#                 stack.append(1)
#             elif i > 2:
#                 stack.append(stack[i-2]+(2**(i//2-1)))
#         if i % 2: # 홀수
#             if i == 1:
#                 stack.append(2)
#             elif i == 3:
#                 stack.append(3)
#             elif i>3:
#                 stack.append(stack[i-4]+stack[i-2])
#     a = []
#     for i in range(len(stack)):
#         if i % 2 == 0: # 짝수일 때
#             if i == 0:
#                 a.append(1)
#             else:
#                 for j in range(2**(i//2)-1):
#                     a.append(a[-1]+1)
#         else:
#             if i == 1:
#                 a.append(2)
#                 a.append(2)
#             elif i == 3:
#                 a.append(4)
#                 a.append(4)
#                 a.append(4)
#             else:
#                 for j in range(stack[i]):
#                     a.append(2**(i//2+1))
#     A = a[N-1]


