# https://www.hackerrank.com/challenges/separate-the-chocolate/problem

def is_satisfy_for_k(x, y, n, k):
    return n * n - (x + 1) * (y + 1) <= k


def separate_the_chocolate(m, n, k, chocolate):
    num = {'D': 0, 'T': 0}
    v = []
    for row in range(m):
        v.append([])
        for col in range(n):
            val = chocolate[col + row * n]
            v[row].append(val)
            num['D'] += 1 if val == 'D' else 0
            num['T'] += 1 if val == 'T' else 0
    vecs = ((0, 0, 1, 1, 0), (0, n - 1, 1, -1, 1), (m - 1, 0, -1, 1, 1), (m - 1, n - 1, -1, -1, 0))
    res = 0
    stop = {'D': False, 'T': False}
    for vec in vecs:
        colors = ('D', 'T') if v[vec[0]][vec[1]] == 'U' else (v[vec[0]][vec[1]])
        cnum = {}
        for color in colors:
            cnum[color] = num[color]
            row = vec[0]
            x_max = n - vec[4]
            for y in range(m - vec[4]):
                col = vec[1]
                for x in range(x_max):
                    cnum[color] -= 1 if v[row][col] == color else 0
                    if row != vec[0] and col != vec[1]:  # then doing analyzing of move
                        if v[row][col] != 'U' and color != v[row][col]:
                            x_max = x
                            break
                        if cnum[color] == 0:
                            if is_satisfy_for_k(x, y, n, k):
                                res += 1
                            print("x: %d, y: %d" % (x, y))
                    col += vec[3]
                row += vec[2]

            one_num = 1 if v[vec[0]][vec[1]] == color else 0
            if num[color] - one_num == 0:
                if is_satisfy_for_k(0, 0, n, k) and not stop[color]:
                    res += 1
                    if n == 1:
                        stop[color] = True
    return res
    # TODO need to consider that there are no squares in summary
    # TODO need to consider parameter k


print(separate_the_chocolate(1, 1, 1, 'U'))
print(separate_the_chocolate(2, 2, 0, 'UUUU'))
print(separate_the_chocolate(3, 3, 6, 'UUUUUUUUU'))
