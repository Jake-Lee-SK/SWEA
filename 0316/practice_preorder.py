N = 13

input_string = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'


def get_tree(string):
    #        p, l, r
    tree = [[0, 0, 0] for _ in range(N+1)]
    inputs = list(map(int, input_string.split()))
    for idx in range(len(inputs) // 2):
        p = inputs[idx*2]
        c = inputs[idx*2 + 1]
        if tree[p][1]:
            tree[p][2] = c
        else:
            tree[p][1] = c

        tree[c][0] = p
    return tree


def pre_order(node):
    if node != 0:
        left, right = tree[node][1], tree[node][2]

        print(node, end=' ')
        pre_order(left)
        pre_order(right)


def in_order(node):
    if node != 0:
        left, right = tree[node][1], tree[node][2]

        in_order(left)
        print(node, end=' ')
        in_order(right)


def post_order(node):
    if node != 0:
        left, right = tree[node][1], tree[node][2]

        post_order(left)
        post_order(right)
        print(node, end=' ')


tree = get_tree(input_string)
pre_order(1)
print()
in_order(1)
print()
post_order(1)



