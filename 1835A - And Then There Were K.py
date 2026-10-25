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
        ans = 1
        while ans * 2 <= n:
            ans *= 2
        out.append(str(ans - 1))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
