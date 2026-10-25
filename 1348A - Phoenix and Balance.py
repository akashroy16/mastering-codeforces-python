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
        ans = (1 << (n // 2 + 1)) - 2
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
