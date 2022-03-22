""" permutations 함수를 import 해서 사용하기
from itertools import permutations

numbers = [1,2,3,4]

# numbers P 4
for perm in permutations(numbers):
    print(perm)

# numbers P n
for perm in permutations(numbers, 3):
    print(perm)
"""

# N개의 숫자에 대한 조합의 경우의 수를 구하는 법은?
#1. bit연산자를 이용
#2. combinations 함수를 이용
#3. DFS를 이용한 recursive?

def combinate(idx):
    if idx == len(numbers):

        return

    result[idx] = True # idx 위치에 해당하는 자리에 True를 넣는다.
    combinate(idx+1) # result 안에서 오른쪽으로 이동하면서 True를 넣는다.
    # 상황 그래프의끝에 이동했다면, 그 바로 전으로 돌아가 False를 넣는다.
    result[idx] = False
    combinate(idx+1) # 그 다음 경우의 수로 이동해서 판단한다.

numbers = [1,2,3]
N = len(numbers)
result = [None] * N # 만들고자 하는 길이만큼 None 갯수를 설정


combinate(0)
