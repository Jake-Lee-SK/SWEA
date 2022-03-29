import sys
sys.stdin = open('input.txt')

def check_A(array):
    global run_or_triplet_of_A
    for i in range(10):
        cnt = 0
        for j in range(len(array)):
            if i == array[j]:
                cnt += 1
                if cnt ==3:
                    run_or_triplet_of_A += 1
                    return
    for i in range(8):
        cnt = 0
        if i in array and i +1 in array and i+2 in array:
            run_or_triplet_of_A += 1
            return


def check_B(array):
    global run_or_triplet_of_B
    for i in range(10):
        cnt = 0
        for j in range(len(array)):
            if i == array[j]:
                cnt += 1
                if cnt ==3:
                    run_or_triplet_of_B += 1
                    return
    for i in range(8):
        cnt = 0
        if i in array and i +1 in array and i+2 in array:
            run_or_triplet_of_B += 1
            return


T = int(input())
for tc in range(1, T+1):
    matrix = list(map(int, input().split()))
    A = []
    B = []
    run_or_triplet_of_A = 0
    run_or_triplet_of_B = 0
    for i in range(6):
        A.append(matrix[2*i])
        if i >= 2:
            check_A(A)

        if run_or_triplet_of_A>0:
            print(f'#{tc} 1')
            break

        B.append(matrix[2*i+1])
        if i >= 2:
            check_B(B)

        if run_or_triplet_of_B>0:
            print(f'#{tc} 2')
            break

    if run_or_triplet_of_A == 0 and run_or_triplet_of_B == 0:
        print(f'#{tc} 0')

