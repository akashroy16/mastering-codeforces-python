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
        s = int(data[idx+1])
        m = int(data[idx+2])
        idx += 3
        
        intervals = []
        for _ in range(n):
            intervals.append((int(data[idx]), int(data[idx+1])))
            idx += 2
            
        possible = False
        last_end = 0
        for l, r in intervals:
            if l - last_end >= s:
                possible = True
                break
            last_end = r
        if m - last_end >= s:
            possible = True
            
        if possible:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
