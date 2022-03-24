import sys
sys.stdin = open('input2.txt')

# 16진수를 2진수로 바꾸는 딕셔너리
binary = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
         '4':'0100', '5':'0101', '6':'0110', '7':'0111',
         '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
         'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

# 코드의 비율 딕셔너리
code = {'211' : 0, '221' : 1, '122' : 2, '411' : 3, '132' : 4,
        '231' : 5, '114' : 6, '312' : 7, '213' : 8, '112' : 9}

# 곱해진 비율대로 다시 나눠주는 함수(최소만큼 늘어난 것을 다시 나눠주면 됨)
def coding(A, B, C):
    min_number = min(A, B, C)
    mina = A//min_number
    minb = b//min_number
    minc = c//min_number
    return str(mina)+str(minb)+str(minc)

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    # 양옆에 0이 모두 지워지고, 안쪽의 0은 어쩔 수 없이 같이 변환함.
    arr = list(set(input().strip().strip('0') for _ in range(N)))
    # 2진수 형태로 저장할 list를 생성
    lists = ['']*len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            lists[i] += binary[arr[i][j]]
    # result에는 암호 해독을 통해 나오는 비율들을 저장
    result = []
    # 나중에 중복됐는지 확인하기 위한 리스트
    visited = []
    for i in range(len(arr)):
        # 임시로 비율을 저장할 장소
        a = 0
        b = 0
        c = 0
        for j in range(len(lists[i])):
            if lists[i]:
                if lists[i][j] == '1' and b == 0 and c == 0:
                    a += 1
                elif lists[i][j] == '0' and a>0 and c == 0:
                    b += 1
                elif lists[i][j] == '1' and a>0 and b>0:
                    c+= 1
                # 만약 끝이 1이었던 상태에서, 0이 시작될 경우 abc 비율을 저장하고 초기화
                if a>0 and b>0 and c>0 and lists[i][j] == '0':
                    result.append(coding(a,b,c))
                    a = 0
                    b = 0
                    c = 0
                # 끝부분에 다다라서도 다시 추가.
                elif j == len(lists[i])-1 and a>0 and b>0 and c>0:
                    result.append(coding(a,b,c))
    cnt = 0
    for i in range(0, len(result), 8):
        result2 = []
        result3 = 0
        # result2에 임시로 코드로 변환한 숫자를 추가
        for j in range(i, i+8):
            result2.append(code[result[j]])
        for j in range(7):
            if j % 2: # 짝수일 때
                result3 += result2[j]
            else:
                result3 += result2[j]*3
        # result3는 맞는 코드인지 확인하기 위한 임시 숫자
        result3 += result2[7]
        # 올바른 코드라면 올바른 코드를 visited 리스트에 추가.
        # 중복되는 코드라면 추가하지 않음.
        if result3%10 == 0 and result2 not in visited:
            visited.append(result2)
        else:
            continue
        # 올바른 코드들의 자릿수별 값을 cnt에 추가해줌.
    for i in range(len(visited)):
        for j in range(8):
            cnt += visited[i][j]
        # 출력
    print(f'#{tc} {cnt}')


