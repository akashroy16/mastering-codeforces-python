import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    if n == 0:
        print(1)
        return
    cycle = [8, 4, 2, 6]
    print(cycle[(n - 1) % 4])

if __name__ == '__main__':
    solve()
