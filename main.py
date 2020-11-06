# https://www.hackerrank.com/challenges/separate-the-chocolate/problem


def separate_the_chocolate(m, n, k, chocolate):
    v = []
    for row in range(m):
        v.append([])
        for col in range(n):
            v[row].append(chocolate[col+row*n])
    return 0


print(separate_the_chocolate(2, 2, 4, 'UUUU'))
