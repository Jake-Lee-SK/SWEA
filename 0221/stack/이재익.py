# 파이썬 안에 구현되어 있는 것들이 많지만, 기본적으로 어떤 개념들이 존재하는 지 알고는 있어야 한다.
# 그래서 만들어보는 것이다.

class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.top = -1 # 없다

    def is_empty(self):
        # if self.top == -1: # 비어있으면(Top이 -1이면)
            # return True
        # else:
            # return False
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):
        if self.is_full():
            raise ValueError('Stack Overflow!')
        else:
            self.top += 1 # top이 index 요소였던 것이고
            self.items[self.top] = item # index를 올림과 동시에 items에 item을 추가함.

    def pop(self): # top을 제거하고 제거한 값을 반환
        if self.is_empty():
            raise ValueError('Empty Stack. Nothing to pop.')
        else:
            item = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return item

    def peek(self): # 제일 위의 값을 반환
        if self.is_empty():
            raise ValueError('Empty Stack.')
        else:
            return self.items[self.top]

    def __str__(self):
        result = '\n-----'
        for item in self.items:
            if item is None:
                result = f'\n|   |' + result
            else:
                result = f'\n| {item} |' + result
        return result

# 함수나 코드를 짤 때 의사함수, 의사코드를 우선 짜볼 것

s1 = Stack(5) # 사이즈가 5인 스택을 생성한다.
s1.is_empty() # True
s1.push(1)
s1.is_empty() # False
s1.push(2)
s1.push(3)
s1.peek() # 3 # peek은 맨 위에 있는 요소를 반환
s1.push(4)
s1.is_full() # False
s1.push(5)
s1.is_full() # True
s1.pop() # 5
s1.pop() # 4
s1.pop() # 3
print(s1)

# 가장 간단한 재귀함수?

def f(i, N):
    if i == N:
        print(B)
    else:
        B[i] = A[i]
        f(i+1, N)

A = [10, 20, 30]
B = [0]*3
f(0, 3)
