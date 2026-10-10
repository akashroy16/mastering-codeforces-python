import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    days = 0
    while n > 0:
        days += 1
        n -= 1
        if days % m == 0:
            n += 1
    print(days)

if __name__ == '__main__':
    solve()
