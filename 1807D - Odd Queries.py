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
        q = int(data[idx+1])
        a = [int(x) for x in data[idx+2 : idx+2+n]]
        idx += 2 + n
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + a[i]
            
        total_sum = pref[n]
        
        for _ in range(q):
            l = int(data[idx])
            r = int(data[idx+1])
            k = int(data[idx+2])
            idx += 3
            
            replaced_sum = pref[r] - pref[l-1]
            new_sum = total_sum - replaced_sum + (r - l + 1) * k
            
            if new_sum % 2 != 0:
                out.append("YES")
            else:
                out.append("NO")
                
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
