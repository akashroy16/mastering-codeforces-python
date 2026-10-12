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
        x = int(data[idx+1])
        a = [int(v) for v in data[idx+2:idx+2+n]]
        idx += 2 + n
        
        low = 1
        high = max(a) + x
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            needed = sum(max(0, mid - val) for val in a)
            if needed <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
