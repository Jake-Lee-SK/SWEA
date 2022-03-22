import sys
sys.stdin = open('input.txt')


def Nods(Tree):
    while 1:
        for Nod in Tree:
            if type(Tree['1']) == str: # 정점 노드에 최종 값이 저장되면 리턴
                return print(f'#{tc} {Tree["1"]}')

            if type(Tree[Nod]) == tuple: # 아직 계산이 이루어지기 전의 노드라면
                if type(Tree[Tree[Nod][1]]) == str and type(Tree[Tree[Nod][2]]) == str: # 계산할 수 있는 노드부터 계산
                    a = int(Tree[Tree[Nod][1]])
                    b = int(Tree[Tree[Nod][2]])
                    if Tree[Nod][0] == '-':
                        Tree[Nod] = str(a - b)
                    elif Tree[Nod][0] == '+':
                        Tree[Nod] = str(a + b)
                    elif Tree[Nod][0] == '*':
                        Tree[Nod] = str(int(a * b))
                    elif Tree[Nod][0] == '/':
                        Tree[Nod] = str(int(a // b))
                    # 계산해서 값을 그 노드에 저장함. 이후 계산할 수 있는 값이 되면 다시 어떤 노드가 작동함.
            else:
                continue

T = 10
for tc in range(1, T+1):
    N = int(input())
    M = [input().split() for _ in range(N)]
    Tree = {}
    for i in range(N):
        if len(M[i]) == 2:
            Tree[M[i][0]] = M[i][1]
        else:
            Tree[M[i][0]] = M[i][1], M[i][2], M[i][3]
    Nods(Tree)