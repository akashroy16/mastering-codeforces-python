import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        if n < 4 or n % 2 != 0:
            out.append("-1")
        else:
            min_b = (n + 5) // 6
            max_b = n // 4
            out.append(f"{min_b} {max_b}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
