import sys
from collections import defaultdict

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
        b = [int(x) for x in data[idx+1+n:idx+1+2*n]]
        idx += 1 + 2 * n
        
        def get_max_runs(arr):
            res = defaultdict(int)
            curr = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i-1]:
                    curr += 1
                else:
                    res[arr[i-1]] = max(res[arr[i-1]], curr)
                    curr = 1
            res[arr[-1]] = max(res[arr[-1]], curr)
            return res
            
        map_a = get_max_runs(a)
        map_b = get_max_runs(b)
        
        ans = 0
        all_keys = set(map_a.keys()).union(set(map_b.keys()))
        for key in all_keys:
            ans = max(ans, map_a[key] + map_b[key])
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
