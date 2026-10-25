import sys
import bisect

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
        q = int(data[idx+1])
        a = [int(x) for x in data[idx+2:idx+2+n]]
        queries = [int(x) for x in data[idx+2+n:idx+2+n+q]]
        idx += 2 + n + q
        
        pref = [0] * (n + 1)
        max_a = [0] * n
        curr_max = 0
        for i in range(n):
            pref[i+1] = pref[i] + a[i]
            curr_max = max(curr_max, a[i])
            max_a[i] = curr_max
            
        ans = []
        for k in queries:
            pos = bisect.bisect_right(max_a, k)
            ans.append(str(pref[pos]))
        out.append(" ".join(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
