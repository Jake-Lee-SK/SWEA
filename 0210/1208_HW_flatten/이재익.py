import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    for i in range(len(boxes)): # 버블 소팅으로 순차배열
        for j in range(len(boxes)-i-1):
            if boxes[j] > boxes[j+1]:
                boxes[j] , boxes[j+1] = boxes[j+1], boxes[j]
    cnt = 0
    while cnt < N: # 카운트가 끝날 때까지
        if boxes[0] < boxes[99]: #최대치에서 최소치에 하나씩 더하고
            boxes[99] -= 1
            boxes[0] += 1
            cnt += 1
        for i in range(len(boxes)):  # 다시 버블 소팅으로 순차배열
            for j in range(len(boxes) - i - 1):
                if boxes[j] > boxes[j + 1]:
                    boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
    print(f'#{tc} {boxes[99]-boxes[0]}')