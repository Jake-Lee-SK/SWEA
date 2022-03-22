import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    tc = int(input())
    word = input()
    sentence = input()
    count_answer = 0


    for i in range(len(sentence)-len(word)+1):
        sentence2 = []
        for j in range(len(word)):
            sentence2.append(sentence[i+j])
        count_same = 0
        for k in range(len(word)):
            if word[k] == sentence2[k]:
                count_same += 1
        if count_same == len(word):
            count_answer += 1

    print(f'#{tc} {count_answer}')