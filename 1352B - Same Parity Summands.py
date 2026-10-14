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
        k = int(data[idx+1])
        idx += 2
        
        if n >= k and (n - (k - 1)) % 2 != 0:
            out.append("YES")
            res = [1] * (k - 1) + [n - (k - 1)]
            out.append(" ".join(map(str, res)))
        elif n >= 2 * k and (n - 2 * (k - 1)) % 2 == 0:
            out.append("YES")
            res = [2] * (k - 1) + [n - 2 * (k - 1)]
            out.append(" ".join(map(str, res)))
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
