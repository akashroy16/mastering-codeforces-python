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
        x = int(data[idx])
        n = int(data[idx + 1])
        m = int(data[idx + 2])
        idx += 3
        while n > 0 and x > 20:
            x = x // 2 + 10
            n -= 1
        if x <= m * 10:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
