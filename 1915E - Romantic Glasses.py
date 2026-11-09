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
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        for i in range(n):
            if i % 2 == 1:
                a[i] = -a[i]
        seen = {0}
        curr = 0
        found = False
        for x in a:
            curr += x
            if curr in seen:
                found = True
                break
            seen.add(curr)
        out.append("YES" if found else "NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
