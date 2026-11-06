import sys
from collections import Counter

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
        s = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        counts = Counter(s)
        possible = True
        for count in counts.values():
            if count == 1:
                possible = False
                break
                
        if not possible:
            out.append("-1")
            continue
            
        p = list(range(1, n + 1))
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            # Shift indices within the group [i, j-1] by 1 to the right
            group_p = p[i:j]
            group_p = [group_p[-1]] + group_p[:-1]
            p[i:j] = group_p
            i = j
        out.append(" ".join(map(str, p)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
