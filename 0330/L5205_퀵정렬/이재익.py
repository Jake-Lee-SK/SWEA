import sys
sys.stdin = open('input.txt')

def quicksort(left, right):
    if left >= right:
        return
    # left를 pivot으로 택한 후, pivot과 right 사이의 숫자를 비교함
    print(A, left, right)
    pivot = left
    i = left +1
    j = right -1
    # 왼쪽에서 두번째 숫자가 오른쪽에서 두번째 숫자보다 작거나 같을 때
    while i <= j:
        while i<= j and A[pivot] >= A[i]:
            i += 1
        while i <= j and A[pivot] <= A[j]:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[pivot], A[j] = A[j], A[pivot]

    quicksort(left, j)
    quicksort(j+1, right)

for tc in range(1, int(input())+1):
    N = int(input())
    A = list(map(int,input().split()))
    # 최초 pivot으로 0을 선정함
    left = 0
    right = len(A)
    quicksort(left, right)
    print(f'#{tc} {A[N//2]}')