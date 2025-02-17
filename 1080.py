import sys

def arr_solution():
    input_function = sys.stdin.readline

    n, m = map(int, input_function().split())
    a = [list(map(int, list(input_function().strip()))) for _ in range(n)]
    b = [list(map(int, list(input_function().strip()))) for _ in range(n)]

    def flip(i, j):
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                a[x][y] = 1 - a[x][y]

    count = 0

    if n < 3 or m < 3:
        print(0 if a == b else -1)
        return

    for i in range(n - 2):
        for j in range(m - 2):
            if a[i][j] != b[i][j]:
                flip(i, j)
                count += 1

    print(count if a == b else -1)

if __name__ == '__main__':
    arr_solution()
