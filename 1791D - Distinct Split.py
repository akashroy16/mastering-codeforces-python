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
        s = data[idx+1]
        idx += 2
        pref = [0] * n
        suff = [0] * n
        
        seen_pref = set()
        for i in range(n):
            seen_pref.add(s[i])
            pref[i] = len(seen_pref)
            
        seen_suff = set()
        for i in range(n - 1, -1, -1):
            seen_suff.add(s[i])
            suff[i] = len(seen_suff)
            
        ans = max(pref[i] + suff[i+1] for i in range(n - 1))
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
