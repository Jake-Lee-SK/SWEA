import sys
sys.stdin = open('input.txt')

n = int(input())
print(n)

numbers = list(map(int, input().split()))
print(numbers)

m = int(input())
print(m)

for number in range(m):
