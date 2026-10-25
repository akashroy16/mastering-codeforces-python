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
        a = [int(x) for x in data[idx+2:idx+2+n]]
        b = [int(x) for x in data[idx+2+n:idx+2+2*n]]
        idx += 2 + 2 * n
        
        max_total = 0
        current_sum = 0
        max_b = 0
        for i in range(min(n, k)):
            current_sum += a[i]
            max_b = max(max_b, b[i])
            total = current_sum + max_b * (k - (i + 1))
            max_total = max(max_total, total)
        out.append(str(max_total))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
