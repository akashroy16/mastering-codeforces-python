import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    x1, y1, x2, y2 = map(int, data[:4])
    if x1 == x2:
        d = abs(y2 - y1)
        print(f"{x1 + d} {y1} {x2 + d} {y2}")
    elif y1 == y2:
        d = abs(x2 - x1)
        print(f"{x1} {y1 + d} {x2} {y2 + d}")
    elif abs(x2 - x1) == abs(y2 - y1):
        print(f"{x1} {y2} {x2} {y1}")
    else:
        print("-1")

if __name__ == '__main__':
    solve()
