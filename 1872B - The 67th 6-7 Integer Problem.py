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
        ans = float('inf')
        for _ in range(n):
            d = int(data[idx])
            s = int(data[idx+1])
            idx += 2
            max_k = d + (s - 1) // 2
            ans = min(ans, max_k)
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
