def tree_insert(tree, node, semi_answer):
    if tree[0] == 0:
        tree.append(node + [-1, -1])
        tree[0] = 1
        semi_answer[node[1]] = 0
        return 0

    val, index = node
    counter = 0
    current = 1

    while True:
        counter += 1

        if index < tree[current][1]:
            if tree[current][2] != -1:
                current = tree[current][2]
            else:
                tree.append(node + [-1, -1])
                tree[current][2] = (len(tree) - 1)
                break

        elif index > tree[current][1]:
            if tree[current][3] != -1:
                current = tree[current][3]
            else:
                tree.append(node + [-1, -1])
                tree[current][3] = (len(tree) - 1)
                break

    semi_answer[index] = counter


def task1(t, data):
    answer = []

    for i in range(t):
        n, line = data[i]
        semi_answer = [-1 for i in range(len(line))]
        tree = [0]
        new_line = [[line[j], j] for j in range(len(line))]
        new_line = sorted(new_line, reverse=True)

        for j in range(len(new_line)):
            tree_insert(tree, new_line[j], semi_answer)
        answer.append(semi_answer)
        
    return answer


result = task1(3, [[5, [3, 5, 2, 1, 4]], [1, [1]], [4, [4, 3, 1, 2]]])
print(result)
