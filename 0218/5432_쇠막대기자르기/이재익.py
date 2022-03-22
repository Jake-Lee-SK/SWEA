import sys
sys.stdin = open('input.txt')

# timeout

T = int(input())
for tc in range(1, T+1):
    # 끝은 '(' 혹은 ')' 이고, 레이저는 ()가 연결되어 있음.
    # 우선 몇 층으로 이루어 졌는지 갯수를 세는 것이 중요함.
    N = list(input())
    sticks = 0
    for i in range(len(N)-1):
        if N[i]=='(' and N[i+1]==')':
            N[i] = 0
            N[i+1] = 0
    layer_tool = []
    # 레이어를 설정해서, 몇 겹으로 이루어져 있는지 계산
    for layer in range(len(N)):
        layer_tool.append(layer)
        if '(' in N:
            for i in range(len(N)-1):
                for j in range(i+1, len(N)):
                    if N[i] in layer_tool and N[i-1] == '(' and N[j] == ')':
                        N[i-1] = layer+1
                        N[j] = layer+1
                        break
                    if N[i] in layer_tool and N[i-1] == '(' and N[j] == '(':
                        break
    # 레이어 사이의 레이저 갯수를 세서, 그만큼 잘린 것이라고 생각.
    for layer in range(max(N), 0, -1):
        layers = []
        for i in range(len(N)):
            if N[i] == layer:
                layers.append(i)
        for k in range(int(len(layers)/2)):
            laser = 0
            for o in range(layers[2*k], layers[2*k+1]):
                if N[o] == 0:
                    laser += 1
            sticks += int(laser/2)+1

    print(f'#{tc} {sticks}')