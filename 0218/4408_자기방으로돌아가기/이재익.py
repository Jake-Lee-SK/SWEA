import sys
sys.stdin = open('input.txt')

# 오류가 나는 코드
# 작은 수~큰수 까지의 숫자를 저장함
def numbers(number1, number2):
    room = []
    if number1 < number2:
        for i in range(number1, number2+1):
            room.append(i)
    if number1 > number2:
        for i in range(number2, number1+1):
            room.append(i)
    return room

#금지되는 시작점과 끝점을 계산함
def no_move(number1, number2):
    no_move_room = []
    if number1 < number2:
        if number1 % 2 == True:  # 홀수면 시작점 그 자체
            no_move_room.append(number1)
        else:  # 짝수면 -1 해줘야 시작점이 됨
            no_move_room.append(number1-1)
        if number2 % 2 == True:  # 목적지가 홀수면 끝점은 홀수+1
            no_move_room.append(number2+1)
        else:  # 짝수면 그냥 그 자체가 끝점
            no_move_room.append(number2)
    if number1 > number2:
        if number2 % 2 == True:  # 홀수면 시작점 그 자체
            no_move_room.append(number2)
        else:  # 짝수면 +1 해줘야 시작점이 됨
            no_move_room.append(number2+1)
        if number1 % 2 == True:  # 목적지가 홀수면 끝점은 홀수+1
            no_move_room.append(number1+1)
        else:  # 짝수면 그냥 그 자체가 끝점
            no_move_room.append(number1)
    return(numbers(no_move_room[0], no_move_room[1]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    std_numbers = numbers(0, N-1)
    move_cnt = 0
    for i in range(N):
        if i in std_numbers:
            move_cnt += 1
            for j in range(N):
                hoxy = 0
                if rooms[j][0] % 2 : # 시작점이 홀수일때
                    if rooms[j][0] in no_move(rooms[i][0], rooms[i][1]):
                        hoxy += 1
                    if rooms[j][0] in no_move(rooms[i][0], rooms[i][1]):
                        continue
                else: # 시작점이 짝수일 때
                    if rooms[j][0]-1 in no_move(rooms[i][0], rooms[i][1]):
                        hoxy += 1
                    if rooms[j][0]-1 in no_move(rooms[i][0], rooms[i][1]):
                        continue
                if rooms[j][1] % 2 : # 끝점이 홀수일때
                    if rooms[j][1]+1 in no_move(rooms[i][0], rooms[i][1]):
                        hoxy += 1
                    if rooms[j][1]+1 in no_move(rooms[i][0], rooms[i][1]):
                        continue
                else: # 끝점이 짝수일 때
                    if rooms[j][1] in no_move(rooms[i][0], rooms[i][1]):
                        hoxy += 1
                    if rooms[j][1] in no_move(rooms[i][0], rooms[i][1]):
                        continue
                if hoxy>0:
                    continue
                if j in std_numbers and hoxy == 0:
                    std_numbers.remove(j)
            std_numbers.remove(i)
        else:
            continue

    print(f'#{tc} {move_cnt}')
