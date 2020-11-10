import os
import sys

def is_satisfy_for_k(x, y):
    left = n*n - (x+1)*(y+1)
    right = (x+1)*(y+1)
    return abs(left - right) <= k

def separateTheChocolate(chocolate):
    print(chocolate)
    num = {'D': 0, 'T': 0}
    v = chocolate
    for row in range(m):
        #v.append([])
        for col in range(n):
            #val = chocolate[col + row * n]
            #v[row].append(val)
            val = chocolate[row][col]
            num['D'] += 1 if val == 'D' else 0
            num['T'] += 1 if val == 'T' else 0
    vecs = ((0, 0, 1, 1, 0), (0, n - 1, 1, -1, 1), (m - 1, 0, -1, 1, 1), (m - 1, n - 1, -1, -1, 0))
    if n == 1:
        vecs = [(0, 0, 1, 1, 0)]
    res = 0
    for vec in vecs:
        colors = ('D', 'T') if v[vec[0]][vec[1]] == 'U' else (v[vec[0]][vec[1]])
        cnum = {}
        for color in colors:
            print('COLOR:', color)
            #cnum[color] = num[color]
            row = vec[0]
            x_max = n - vec[4]
            print('VEC:', vec)
            #print('CNUM:', cnum[color])
            for y in range(m - vec[4]):  # - vec[4]):
                col = vec[1]
                cnum = 0
                cnumx = [0 for cx in range(x_max)]
                for x in range(x_max):
                    if x == n-1 and y == m-1 and n>1 and m>1:
                        break
                    cnum += cnumx[x]
                    if v[row][col] == color:
                        cnum += 1
                        cnumx[x] += 1
                    #cnum[color] -= 1 if v[row][col] == color else 0
                    print('x: %d, y: %d, Row: %d, Col: %d, Cnum: %d' % (x, y, row, col, cnum), end=', ')
                    if v[row][col] != 'U' and color != v[row][col]:
                        x_max = x
                        print()
                        break
                    if cnum == num[color]:
                        if is_satisfy_for_k(x, y):
                            if vecs.index(vec) == 3 and (x == n-1 or y == m-1):
                                res -= 1
                                print("-1")
                            res += 1
                            print(' +1', end='')
                    col += vec[3]
                    print()
                row += vec[2]
            print(res)
    return res

if __name__ == '__main__':

    m = 2
    n = 2
    k = 3
    chocolate = ['UT', 'TU']
    #result = separateTheChocolate(chocolate)

    m = 2
    n = 2
    k = 4
    chocolate = ['UU', 'UU']
    #result = separateTheChocolate(chocolate)

    m = 1
    n = 1
    k = 1
    chocolate = ['T']
    #result = separateTheChocolate(chocolate)

    m = 1
    n = 2
    k = 1
    chocolate = ['UU']
    #result = separateTheChocolate(chocolate)

    m = 4
    n = 3
    k = 5
    chocolate = ['TTT', 'TUD', 'UDD', 'UUU']
    #result = separateTheChocolate(chocolate)

    m = 3
    n = 3
    k = 9
    chocolate = ['UUU', 'UDU', 'UTU']       # 13
    result = separateTheChocolate(chocolate)
