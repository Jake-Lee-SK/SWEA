import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1_count_list = [0]*len(str1)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                str1_count_list[i] += 1
    count_max = 0
    for i in str1_count_list:
        if i > count_max:
            count_max = i
    print(f'#{tc} {count_max}')
