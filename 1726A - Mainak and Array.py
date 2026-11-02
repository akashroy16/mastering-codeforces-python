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
        
        if n == 1:
            out.append("0")
            continue
            
        ans = a[-1] - a[0]
        for i in range(n):
            ans = max(ans, a[i] - a[(i + 1) % n])
        for i in range(1, n):
            ans = max(ans, a[i] - a[0])
        for i in range(n - 1):
            ans = max(ans, a[-1] - a[i])
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
