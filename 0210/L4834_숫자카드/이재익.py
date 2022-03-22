import sys
sys.stdin = open('input.txt')

def my_max(nums):
    num = nums[0]
    for i in nums:
        if i > num:
            num = i
    return num

t = int(input()) # tc 갯수
for tc in range(1, t+1): #tc 당 프린트해야 하기 때문에, for문 사용
    N = int(input()) # 카드 갯수
    a = input() # iterable해야하기 때문에 str 형태
    many_num = 0 # 카드 이름?
    count_num = 0 # 카드 갯수
    num_list = [] # count 함수를 거치고 나서 카드 갯수를 저장해 놓는 곳.
    a_str = str(a) # a를 str형태로 변경한 것
    for idx in range(10): # 0~9 자동으로.
        num_list.append(a_str.count(str(idx))) #num_list라는 곳에, a_str에 있는 숫자 갯수 세서 추가하는 것.
    count_num = my_max(num_list) # 최댓값
    dict_num = {}
    for num in range(10):
        dict_num[num] = num_list[num]
    for keys, values in dict_num.items():
        if values == count_num:
            many_num = keys
    print(f'#{tc} {many_num} {count_num}')