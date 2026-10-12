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
        m = int(data[idx+1])
        k = int(data[idx+2])
        b = [int(x) for x in data[idx+3:idx+3+n]]
        c = [int(x) for x in data[idx+3+n:idx+3+n+m]]
        idx += 3 + n + m
        ans = 0
        for x in b:
            for y in c:
                if x + y <= k:
                    ans += 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
