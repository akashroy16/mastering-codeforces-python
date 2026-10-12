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
        ans = 0
        for i in range(1, 10):
            val = i
            while val <= n:
                ans += 1
                val = val * 10 + i
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
