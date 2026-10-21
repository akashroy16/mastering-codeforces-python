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
        sorted_s = sorted(s, reverse=True)
        m1 = sorted_s[0]
        m2 = sorted_s[1]
        res = []
        for x in s:
            if x == m1:
                res.append(str(x - m2))
            else:
                res.append(str(x - m1))
        out.append(" ".join(res))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
