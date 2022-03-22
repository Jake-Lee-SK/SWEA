import sys
sys.stdin = open('input.txt')

def get_tree(data):
    tree = [[0,0,0] for _ in range(N+1)]
            #p, l, r
    for idx in range(len(data)):
        if len(data[idx])>3:
            tree[idx+1][0] = data[idx][2]
            tree[idx+1][1] = data[idx][1]
            tree[idx+1][2] = data[idx][3]
        elif len(data[idx]) == 3:
            tree[idx+1][1] = data[idx][1]
            tree[idx+1][2] = data[idx][2]
        else:
            tree[idx+1][1] = data[idx][1]
    return tree

def in_order(node):
    global stack
    global visit
    if 0<node<=N:
        if visit[node] == False:
            in_order(node*2)
            visit[node] = True
            stack.append(tree[node][1])
            in_order(node*2+1)

for tc in range(1, 11):
    N = int(input())
    M = [list(input().split()) for i in range(N)]
    tree = get_tree(M)
    stack = []
    visit = [False] * (N+1)
    in_order(1)
    k = ''.join(stack)
    print(f'#{tc} {k}')