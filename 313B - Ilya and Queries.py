import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    s = data[0]
    n = len(s)
    pref = [0] * n
    for i in range(1, n):
        pref[i] = pref[i-1] + (1 if s[i-1] == s[i] else 0)
    m = int(data[1])
    idx = 2
    out = []
    for _ in range(m):
        l = int(data[idx])
        r = int(data[idx+1])
        idx += 2
        out.append(str(pref[r-1] - pref[l-1]))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
