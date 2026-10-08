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
        s = [int(x) for x in data[idx:idx+4]]
        idx += 4
        m1 = max(s[0], s[1])
        m2 = max(s[2], s[3])
        s.sort()
        if (m1 == s[2] and m2 == s[3]) or (m1 == s[3] and m2 == s[2]):
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
