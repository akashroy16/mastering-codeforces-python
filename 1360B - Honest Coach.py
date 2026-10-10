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
        s = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        s.sort()
        min_diff = min(s[i+1] - s[i] for i in range(n - 1))
        out.append(str(min_diff))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
