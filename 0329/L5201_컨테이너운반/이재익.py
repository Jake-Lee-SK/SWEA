import sys
sys.stdin = open('input.txt')

# 화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.

# 트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.

# 컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.

# 이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.

# 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 짐의 숫자, M은 트럭의 숫자
    container = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))
    # 최대로 실을 수 있는 적재량보다 가장 가벼운 무게가 더 크다면

    if trucks[-1] < container[0]:
        # 0을 출력함
        print(f'#{tc} 0')

    # 실을 수 있는 짐이 있다면

    else:
        # ton에 지금까지 옮긴 짐의 총량을 저장.
        ton = 0
        # 트럭의 무게를 거꾸로 순회하면서
        for i in range(M):
            # weight에서 가장 무거운 것부터 탐색하면서, 트럭 적재량과 같거나 가장 가깝게 무거운 것을 적재함
            for j in range(len(container)):
                if trucks[-i-1] >= container[-j-1]:
                    ton += container[-j-1]
                    # 적재한 후에는 짐 리스트에서 삭제
                    container.remove(container[-j-1])
                    # 적재한 후에는 다음 트럭을 탐색
                    break
        print(f'#{tc} {ton}')
