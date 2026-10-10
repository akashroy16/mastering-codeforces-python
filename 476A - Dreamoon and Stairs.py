import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    min_moves = (n + 1) // 2
    if min_moves % m != 0:
        min_moves += m - (min_moves % m)
    if min_moves <= n:
        print(min_moves)
    else:
        print("-1")

if __name__ == '__main__':
    solve()
