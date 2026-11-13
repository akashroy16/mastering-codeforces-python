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
        evens = sum(1 for x in a if x % 2 == 0)
        odds = n - evens
        if evens % 2 == 0 and odds % 2 == 0:
            out.append("YES")
        else:
            a.sort()
            has_adj = False
            for i in range(n - 1):
                if a[i + 1] - a[i] == 1:
                    has_adj = True
                    break
            if has_adj:
                out.append("YES")
            else:
                out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
