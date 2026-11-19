import sys

def can_make(n, m):
    if n == m:
        return True
    if n < m or n % 3 != 0:
        return False
    return can_make(n // 3, m) or can_make(2 * (n // 3), m)

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
        m = int(data[idx + 1])
        idx += 2
        out.append("YES" if can_make(n, m) else "NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
