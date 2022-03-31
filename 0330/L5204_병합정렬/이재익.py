import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
def merge_sort(m):
    # 나눠서 1이 되면 나누는 것을 그만하고 값을 나눠줌
    if len(m) == 1:
        return m
    # 1이 될때까지 나눠줌
    mid = len(m)//2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])
    return merge(left, right)

def merge(left, right):
    global biggerleft
    # 만약 왼쪽 끝이 오른쪽끝보다 크면 1을 더함
    if left[-1] > right[-1]:
        biggerleft += 1
    result = []
    # 최초 idx를 정해줌
    left_idx, right_idx = 0, 0
    # left와 right의 길이만큼을 정함
    n, m = len(left), len(right)
    # 최초 idx가 길이만큼까지 길어지면 그만둠
    while left_idx != n and right_idx != m:
        # 비교해서 작은 쪽을 result에 추가함
        # 추가한 후 idx를 하나 올려줘서 다음 거랑 비교하게 만듦
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    # 만약 idx 숫자가 부족한 쪽이 있다면 숫자가 큰 쪽이므로 result 왼쪽에 추가함
    if left_idx != n:
        result += left[left_idx:]
    if right_idx != m:
        result += right[right_idx:]
    return result
T=int(input())
for tc in range(1, T+1):
    N = int(input())
    M = list(map(int,input().split()))
    biggerleft = 0
    merge_M = merge_sort(M)
    print(f'#{tc} {merge_M[N//2]} {biggerleft}')
