import sys
sys.stdin = open('input.txt')
# import heapq

def find(N):
    global plus
    if N//2 == 1:
        plus.append(tree[N//2])
        return
    else:
        plus.append(tree[N//2])
        find(N//2)

def heapify(index):
    if index == 1:
        return

    parent = index//2

    if 0 < parent < N and tree[index] < tree[parent]: # 부모 노드가 0보다 크고 N보다 작으며, 부모 노드 숫자가 더 클 때
        tree[index], tree[parent] = tree[parent], tree[index] # 자식 노드와 부모노드를 바꿈
        heapify(parent) # 다시 그 부모 노드에도 점검.
    else:
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    # heapq.heapify(M) heapq.heapify()를 사용하면 곧장 리스트가 내림차순 힙으로 변하게 된다.
    tree = [0]*(N+1)
    for i in range(N):
        if i == 0:
            tree[i+1] = M[i]
        else:
            tree[i+1] = M[i]
            heapify(i+1)
    plus = []
    find(N)
    print(f'#{tc} {sum(plus)}')