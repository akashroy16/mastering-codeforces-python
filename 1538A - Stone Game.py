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
        
        min_val = min(a)
        max_val = max(a)
        i1 = a.index(min_val) + 1
        i2 = a.index(max_val) + 1
        
        left = min(i1, i2)
        right = max(i1, i2)
        
        ans = min(right, n - left + 1, left + (n - right + 1))
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
