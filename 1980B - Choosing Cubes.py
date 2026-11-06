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
        f = int(data[idx+1])
        k = int(data[idx+2])
        a = [int(x) for x in data[idx+3:idx+3+n]]
        idx += 3 + n
        
        target_val = a[f - 1]
        a.sort(reverse=True)
        
        if a[k - 1] < target_val:
            out.append("YES")
        elif a[k - 1] > target_val:
            out.append("NO")
        else:
            if k < n and a[k] == target_val:
                out.append("MAYBE")
            else:
                out.append("YES")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
