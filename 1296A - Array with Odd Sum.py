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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        total = sum(a)
        odds = sum(1 for x in a if x % 2 != 0)
        evens = n - odds
        if total % 2 != 0 or (odds > 0 and evens > 0):
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
