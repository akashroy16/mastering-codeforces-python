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
        
        seen = {0}
        curr_sum = 0
        found = False
        for i in range(n):
            if i % 2 == 0:
                curr_sum += a[i]
            else:
                curr_sum -= a[i]
            if curr_sum in seen:
                found = True
                break
            seen.add(curr_sum)
            
        if found:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
