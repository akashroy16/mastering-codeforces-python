import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    b = [int(x) for x in data[1:n+1]]
    max_val = max(b)
    min_val = min(b)
    diff = max_val - min_val
    if diff == 0:
        counts = n * (n - 1) // 2
    else:
        counts = b.count(max_val) * b.count(min_val)
    print(f"{diff} {counts}")

if __name__ == '__main__':
    solve()
