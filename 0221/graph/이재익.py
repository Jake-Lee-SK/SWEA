import sys
sys.stdin = open('input.txt')

def DFS(S):
    global where # 갔던 곳을 정리하기 위해 where를 글로벌인자 선언
    visited = [] # 이미 갔는지 확인하는 stack에 쌓아두는 곳
    # 이동하면 초기화됨
    where.append(S) # 갔던 곳을 저장함
    visited.append(S) # 스택에 S로 저장된 값을 쌓음
    for i in L[S]: # L 안의 S의 edge와 연결된 장소에 대해서
        if i not in visited:
            DFS(i) # i로 다시 DFS(깊이우선탐색)를 시작
    # 차례대로 첫번째로 주어진 곳의
    # 1번째, 1번째, 1번째 장소와 이어지면 그곳을 탐색하고
    # 더 이상 나아갈 곳이 없으면 첫번째로 주어진 곳의 두번째
    # edge와 연결된 Vertex를 탐색.
    # 따라서 방향성 그래프에 대해서도 똑같이 적용 가능하다.


 # Linked List의 경우
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # V = 점 갯수, E = 간선 갯수
    # 이 경우에는 간선 갯수만큼 start,end가 존재.

    # 1. 재귀함수방식(Linked List 방식)
    L = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        L[start].append(end)
    S, G = map(int, input().split())
    # 스택을 쌓아서 DFS를 실행.
    where = []
    DFS(S)
    if G in where:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')