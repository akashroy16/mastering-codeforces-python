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
        a = int(data[idx])
        b = int(data[idx+1])
        n = int(data[idx+2])
        x = [int(v) for v in data[idx+3:idx+3+n]]
        idx += 3 + n
        ans = b
        for item in x:
            ans += min(a - 1, item)
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
